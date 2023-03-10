import ffmpeg

def volume(media, volume: float=1.0):
    """
        takes in a media type object from the Editor file and the width, or an optional height if not provided then the editor will be inteligent enough to add the height with the propotional to the aspect ratio.
    """
    v = media.inp[0]
    a = media.inp[1].filter("volume", volume)

    return [v, a]
