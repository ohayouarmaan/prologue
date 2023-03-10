import ffmpeg

def fadeIn(media,  duration: float, st: float=0):
    v = media.inp[0].filter("fade", t="in", st=st, d=duration)
    a = media.inp[1].filter("afade", t="in", st=st, d=duration)

    return [v, a]

def fadeOut(media,  duration: float, st: float=0):
    if st:
        v = media.inp[0].filter("fade", t="out", st=st, d=duration)
        a = media.inp[1].filter("afade", t="out", st=st, d=duration)
    else:
        v = media.inp[0].filter("fade", t="out", d=duration)
        a = media.inp[1].filter("afade", t="out", d=duration)

    return [v, a]