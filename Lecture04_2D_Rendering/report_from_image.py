from pico2d import *
import os
import math

# 스크립트 파일이 있는 디렉토리로 작업 폴더 변경
os.chdir(os.path.dirname(os.path.abspath(__file__)))

open_canvas()

# 이미지 로드
boy = load_image('character.png')
grass = load_image('grass.png')

def draw_boy(x, y):
    """캐릭터와 배경을 그리는 함수"""
    clear_canvas()
    grass.draw(400, 30)
    boy.draw(x, y)
    update_canvas()
    delay(0.01)

def move_rectangle():
    """사각형 경로로 캐릭터 이동"""
    print("Moving in rectangle path")

    # 아래쪽 가장자리: 왼쪽에서 오른쪽으로
    for x in range(50, 751, 10):
        draw_boy(x, 90)

    # 오른쪽 가장자리: 아래에서 위로
    for y in range(90, 511, 10):
        draw_boy(750, y)

    # 위쪽 가장자리: 오른쪽에서 왼쪽으로
    for x in range(750, 49, -10):
        draw_boy(x, 510)

    # 왼쪽 가장자리: 위에서 아래로
    for y in range(510, 89, -10):
        draw_boy(50, y)

def move_circle():
    """원형 경로로 캐릭터 이동"""
    print("Moving in circle path")

    center_x, center_y = 400, 300
    radius = 200

    # 0도부터 360도까지 원을 그리며 이동
    for degree in range(0, 361, 5):
        radian = math.radians(degree)
        x = center_x + radius * math.cos(radian)
        y = center_y + radius * math.sin(radian)
        draw_boy(x, y)

# 메인 루프
while True:
    move_rectangle()  # 사각형 운동
    move_circle()     # 원 운동

close_canvas()
