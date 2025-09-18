from pico2d import *

open_canvas()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

boy = load_image('character.png')

def Move_rectangle():
    print("Moving rectangle")
    pass

def Move_circle():
    print("Moving circle")

    clear_canvas()
    boy.draw_now(400,300)
    delay(0.1)

    pass

while True:
    Move_rectangle()
    Move_circle()
    break
    pass

close_canvas()