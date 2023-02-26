import ffmpeg
from Editor import Media


def cut(media: Media, _from: int, _to: int):
    pts="PTS-STARTPTS"
    # v = ffmpeg.trim(media.inp[0], start=_from, end=_to)
    # v = media.inp[0].split().trim(start=_from, end=_to)
    print(media.inp[0])
    print(media.inp[1])
    v = media.inp[0].filter("trim", start=_from, end=_to).filter("setpts", pts)
    a = media.inp[1].filter("atrim", start=_from, end=_to).filter("asetpts", pts)

    # c = ffmpeg.concat(v, a, v=1, a=1)
    new_duration = (_to - _from)
    media.duration = new_duration

    return [v, a]
