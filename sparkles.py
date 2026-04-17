import pyglet
import random


how_many_sparkles = 100
speed = 100
size = 50

window = pyglet.window.Window(fullscreen=True, config=pyglet.gl.Config(double_buffer=True))

sparkles = []
for _ in range(how_many_sparkles):
    sparkles.append(pyglet.shapes.Triangle(
        window.width//2, window.height//2,
        window.width//2 + size/2, window.height//2 + size / 2 ** 0.5,
        window.width//2 + size, window.height//2))


@window.event
def on_draw():
    window.clear()
    [t.draw() for t in sparkles]


def bump(x):
    for t in sparkles:
        t.color = (random.randint(150, 250), random.randint(150, 250), random.randint(150, 250))
        t.x = (t.x + random.randint(-speed//2, speed//2)) % window.width
        t.y = (t.y + random.randint(-speed//2, speed//2)) % window.height
        t.rotation += random.randint(-speed, speed)


pyglet.clock.schedule_interval(bump, 0.01)
pyglet.app.run()