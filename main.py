import ffmpeg
from Editor import Editor, Media
from functions import cut

e = Editor()
m = Media("./testfiles/1.mp4")
m2 = Media("./testfiles/2.mp4")

m.apply(cut.cut, {
    "_from": 0,
    "_to": 14
})

m2.apply(cut.cut, {
    "_from": 0,
    "_to": 4
})

e.default_timeline.add(m, _from=3)
e.default_timeline.add(m2, _from=2)

inpts = (e.default_timeline.generate())
v,a = e.default_timeline.render()

x = ffmpeg.concat(v,a, v=1, a=1, n=2)
x = x.output("out.mp4").run()
