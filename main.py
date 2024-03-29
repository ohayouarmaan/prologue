import ffmpeg
from Editor import Editor, Media
from functions import cut, volume, fade

e = Editor()
m = Media("./testfiles/3.mp4")
m2 = Media("./testfiles/2.mp4")

m.apply(cut.cut, {
    "_from": 0,
    "_to": 10
})

m.apply(volume.volume, {
    "volume": 0.5
})

m2.apply(cut.cut, {
    "_from": 0,
    "_to": 4
})

m.apply(fade.fadeIn, {
    "duration": 3,
})

e.default_timeline.add(m)
e.default_timeline.add(m2)

inpts = (e.default_timeline.generate())
v, a = e.default_timeline.render()

x = ffmpeg.concat(v,a, v=1, a=1, n=2)
x = x.output("out.mp4")

with open("test_logs.log", "w") as f:
    f.write(" ".join(x.get_args()))

x.run()
