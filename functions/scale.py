import ffmpeg

def scale(media, width: int, height: int=-1):
    """
        takes in a media type object from the Editor file and the width, or an optional height if not provided then the editor will be inteligent enough to add the height with the propotional to the aspect ratio.
    """
    v = media.inp[0].filter("scale", width, height)
    a = media.inp[1]

    return [v, a]
