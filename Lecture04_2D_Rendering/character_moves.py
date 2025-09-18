from pico2d import *

open_canvas()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

boy = load_image('character.png')

def move_top():
    print('Moving top')
    for x in range(0, 800, 10):
        draw_boy(x, 550)
    pass

def move_right():
    print('Moving right')
    pass

def move_bottom():
    print('Moving bottom')
    pass

def move_left():
    print('Moving left')
    pass

def Move_rectangle():
    print("Moving rectangle")

    move_top()
    move_right()
    move_bottom()
    move_left()

    pass

def Move_circle():
    print("Moving circle")

    r = 200
    for deg in range(0, 360):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)
    pass


def draw_boy(x: float, y: float):
    clear_canvas()
    boy.draw_now(x, y)
    delay(0.1)


while True:
    Move_rectangle()
    Move_circle()
    break
    pass

close_canvas()