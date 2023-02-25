import ffmpeg
from Editor import Editor, Media
from functions import cut

e = Editor()
m = Media("./testfiles/1.mp4")
m.apply(cut.cut, {
    "_from": 0,
    "_to": 4
})
