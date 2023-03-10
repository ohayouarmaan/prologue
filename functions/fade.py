import ffmpeg

def fadeIn(media,  d: float, st: float=0):
    v = media.inp[0].filter("fade", t="in", st=st, d=d)
    a = media.inp[1].filter("afade", t="in", st=st, d=d)

    return [v, a]

def fadeOut(media,  d: float, st: float=0):
    v = media.inp[0].filter("fade", t="out", st=st, d=d)
    a = media.inp[1].filter("afade", t="out", st=st, d=d)

    return [v, a]