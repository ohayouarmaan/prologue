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

e.default_timeline.add(m)
e.default_timeline.add(m2)
inpts = (e.default_timeline.generate())
print(inpts)
v = e.default_timeline.render()

x = ffmpeg.output(v, "out.mp4")
print(x.get_args())
x.run()
