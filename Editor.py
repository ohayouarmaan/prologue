import ffmpeg
import os
import toml

# Helper classes
class Media:
    def __init__(self, path: str, stream=None, duration=None):
        if not stream:
            self.path = path
            self.inp = []
            if(os.path.isfile(self.path)):
                inp = ffmpeg.input(self.path)
                self.inp.append(inp['v'])
                self.inp.append(inp['a'])
            else:
                self.inp = []
                raise FileNotFoundError()
        
            self.duration = float(ffmpeg.probe(self.path)['streams'][0]['duration'])
        else:
            self.inp = stream
            self.path = ""
            self.duration = duration
        
        print(self.inp)


    def toJSON(self) -> object:
        return {
            "path": self.path,
        }
    
    def apply(self, filter, args):
        self.inp = filter(self, **args)

class Timeline:
    def __init__(self, medias: list[Media], default_dimensions=(1920, 1080)):
        self.medias = medias
        self.default_dimensions = default_dimensions
        self.inputs = []
        
    def add(self, media: Media) -> bool:
        if media:
            self.medias.append(media)
            return True
        else:
            return False
    
    def generate(self):
        null_stream_length = 0
        for m in self.medias:
            null_stream_length += m.duration
        
        v_null_stream = ffmpeg.input(f"nullsrc=size={self.default_dimensions[0]}x{self.default_dimensions[1]}", f="lavfi", t=f"{null_stream_length}")
        a_null_stream = ffmpeg.input(f"anullsrc", f="lavfi", t=f"{null_stream_length}")
        self.inputs.append({
            "start": 0,
            "end": null_stream_length,
            "vstream": v_null_stream,
            "astream": a_null_stream
        })

        prev_end = 0
        for m in self.medias:
            self.inputs.append({
                "start": prev_end,
                "end": prev_end + m.duration,
                "vstream": m.inp[0],
                "astream": m.inp[1],
            })

            prev_end = prev_end + m.duration
        
        return self.inputs
    
    def render(self):
        #TODO: delay the audio and video to match the timeline
        self.final_video_stream = self.inputs[0]['vstream']
        self.final_audio_stream = self.inputs[0]['astream']
        for m in self.inputs[1:]:
            self.final_video_stream = ffmpeg.overlay(self.final_video_stream, m['vstream'], enable=f"between(t,{m['start']},{m['end']})")

        return (self.final_video_stream)


class Editor:
    def __init__(self):
        self.config = toml.load("./CONFIGURATION.toml")['Editor_Configurations']
        self.__version__ = self.config['version']
        self.default_timeline = Timeline(medias=[])

if __name__ == "__main__":
    e = Editor()
    print(e.config)
