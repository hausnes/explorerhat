import pgzero

WIDTH = 300
HEIGHT = 300

def draw():
    screen.fill((128, 0, 0))

def update():
    if keyboard.left:
        print("Venstre!")
    if keyboard.right:
        print("Høgre!")
    if keyboard.up:
        print("Opp!")
    if keyboard.down:
        print("Ned!")

def on_mouse_down(pos):
    print("Mus!")

