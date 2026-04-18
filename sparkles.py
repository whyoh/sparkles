import pyglet
import random


how_many_sparkles = 250
speed = 50
size = 80

window = pyglet.window.Window(fullscreen=True, config=pyglet.gl.Config(double_buffer=True))

sparkles = []
for _ in range(how_many_sparkles):
    sparkles.append(pyglet.shapes.Triangle(
        window.width//2, window.height//2,
        window.width//2 + size/2, window.height//2 + size * 0.75 ** 0.5,
        window.width//2 + size, window.height//2))


def bump():
    for t in sparkles:
        t.color = (random.randint(150, 250), random.randint(150, 250), random.randint(150, 250), random.randint(0, 250))
        t.x = (t.x + random.randint(-speed//2, speed//2)) % window.width
        t.y = (t.y + random.randint(-speed//2, speed//2)) % window.height
        t.rotation += random.randint(-speed, speed)


@window.event
def on_draw():
    window.clear()
    [t.draw() for t in sparkles]
    bump()


pyglet.app.run()