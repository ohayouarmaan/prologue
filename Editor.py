# Import statements
import ffmpeg
import os
import toml

# Helper classes
class Media:
    def __init__(self, path: str):
        self.path = path
        if(os.path.isfile(self.path)):
            self.inp = ffmpeg.input(self.path)
        else:
            self.inp = None
            raise FileNotFoundError()

    def toJSON(self) -> object:
        return {
            "path": self.path,
        }
    
    def apply(self, filter, args):
        self.inp = filter(self, **args)

class Timeline:
    def __init__(self, medias: list[Media]):
        self.medias = medias
        
    def add(self, media: Media) -> bool:
        if media:
            self.medias.append(media)
            return True
        else:
            return False

class Editor:
    def __init__(self):
        self.config = toml.load("./CONFIGURATION.toml")['Editor_Configurations']
        self.__version__ = self.config['version']
        self.default_timeline = Timeline(medias=[])

if __name__ == "__main__":
    e = Editor()
    print(e.config)
