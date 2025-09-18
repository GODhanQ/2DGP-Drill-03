from pico2d import *
import os
import math

# Drill #3 제출 - 2024180014 민현규

open_canvas()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

boy = load_image('character.png')
grass = load_image('grass.png')

def move_top():
    print('Moving top')
    for x in range(0, 800, 10):
        draw_boy(x, 550)

def move_right():
    print('Moving right')
    for y in range(550, 0, -10):
        draw_boy(800, y)

def move_bottom():
    print('Moving bottom')
    for x in range(800, 0, -10):
        draw_boy(x, 0)

def move_left():
    print('Moving left')
    for y in range(0, 550, 10):
        draw_boy(0, y)

def Move_rectangle():
    print("Moving rectangle")

    move_top()
    move_right()
    move_bottom()
    move_left()

def Move_circle():
    print("Moving circle")

    r = 200
    for deg in range(0, 360, 5):
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_boy(x, y)

def draw_boy(x: float, y: float):
    clear_canvas()
    grass.draw(400, 30)
    boy.draw(x, y)
    update_canvas()
    delay(0.01)

while True:
    Move_rectangle()
    Move_circle()

close_canvas()
