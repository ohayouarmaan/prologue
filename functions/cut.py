import ffmpeg


def cut(media, _from: int, _to: int):
    pts="PTS-STARTPTS"
    v = media.inp[0].filter("trim", start=_from, end=_to).filter("setpts", pts)
    a = media.inp[1].filter("atrim", start=_from, end=_to).filter("asetpts", pts)

    new_duration = (_to - _from)
    media.duration = new_duration

    return [v, a]
