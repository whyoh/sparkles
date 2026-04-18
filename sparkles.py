import pyglet
import random


how_many_sparkles = 250
size = 80
speed = 25
attraction = -3000
attract = True

limits = {
    "speed": (2, 200),
    "attraction": (-4000, 4000)
}

window = pyglet.window.Window(fullscreen=True, config=pyglet.gl.Config(double_buffer=True))

attractor = window.width // 2, window.height // 2

sparkles = []
for _ in range(how_many_sparkles):
    sparkles.append(pyglet.shapes.Triangle(
        window.width//2, window.height//2,
        window.width//2 + size/2, window.height//2 + size * 0.75 ** 0.5,
        window.width//2 + size, window.height//2))

window.set_mouse_cursor(window.get_system_mouse_cursor(window.CURSOR_HAND))


def bump():
    for t in sparkles:
        t.color = (random.randint(150, 250), random.randint(150, 250), random.randint(150, 250), random.randint(0, 200))
        dx, dy = t.x - attractor[0], t.y - attractor[1]
        dist2 = dx ** 2 + dy ** 2
        pull = 0 if not attract or dist2 < 100 else (attraction / dist2)
        t.x = (t.x + pull * dx + random.randint(-speed//2, speed//2)) % window.width
        t.y = (t.y + pull * dy + random.randint(-speed//2, speed//2)) % window.height
        t.rotation += random.randint(-speed, speed)


@window.event
def on_draw():
    window.clear()
    [t.draw() for t in sparkles]
    bump()


@window.event
def on_mouse_motion(x, y, dx, dy):
    global attractor
    attractor = x, y


@window.event
def on_mouse_release(x, y, buttons, modifiers):
    global attract
    attract = False


@window.event
def on_mouse_drag(x, y, dx, dy, buttons, modifiers):
    global attractor, attract
    attractor = x, y
    attract = True


@window.event
def on_key_press(symbol, modifiers):
    global speed, attraction, attract
    if symbol == pyglet.window.key.Q:
        speed += 10
    if symbol == pyglet.window.key.A:
        speed //= 2
    speed = max(speed, 2)
    if speed % 2:
        speed += 1
    if symbol == pyglet.window.key.SPACE:
        attract = not attract
    if symbol == pyglet.window.key.W:
        attraction -= 2000 if attraction == 1000 else 1000
    if symbol == pyglet.window.key.S:
        attraction += 2000 if attraction == -1000 else 1000
    speed = min(max(speed, limits["speed"][0]), limits["speed"][1])
    attraction = min(max(attraction, limits["attraction"][0]), limits["attraction"][1])
    


pyglet.app.run()