import ffmpeg
from Editor import Media


def cut(media: Media, _from: int, _to: int):
    pts="PTS-STARTPTS"
    v = media.inp.trim(start=_from, end=_to).setpts(pts)
    a = media.inp.filter("atrim", start=_from, end=_to).filter("asetpts", pts)
    c = ffmpeg.concat(v, a, v=1, a=1)
    new_duration = (_to - _from)
    media.duration = new_duration
    return c
