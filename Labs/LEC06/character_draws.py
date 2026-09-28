# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)

boy = load_image('character.png')

clear_canvas()
# 캔버스 안정용
def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            close_canvas()
            raise SystemExit

def move_circle():
    for degree in range(361):
         theta = math.radians(degree)
         x = 400 + 200 * math.cos(theta)
         y = 300 + 200 * math.sin(theta)

         handle_events()
         clear_canvas()
         boy.draw(x, y)
         update_canvas()
         delay(0.01)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()

def move_top():
    print('top')
    pass
def move_right():
    print('right')
    pass

def move_bottom():
    print('bottom')
    pass

def move_left():
    print('left')
    pass

def move_triangle():
    print('triangle')
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()