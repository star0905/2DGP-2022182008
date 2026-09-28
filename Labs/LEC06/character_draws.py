# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)

boy = load_image('character.png')

# 이동 표현 함수
def draw_boy(x, y):
    handle_events()
    clear_canvas()
    boy.draw(x, y)
    update_canvas()
    delay(0.01)

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
    for x in range(50, 751, 5):
     draw_boy(x, 550)

def move_right():
    for y in range(550, 49, -5):
        draw_boy(750, y)

def move_bottom():
    for x in range(750, 49, -5):
        draw_boy(x, 50)

def move_left():
    for y in range(50, 551, 5):
        draw_boy(50, y)

def move_triangle():
    print('triangle')
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()