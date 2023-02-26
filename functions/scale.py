import ffmpeg

def scale(media, width: int, height: int=-1):
    v = media.inp[0].filter("scale", width, height)
    a = media.inp[1]

    return [v, a]
