# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)

boy = load_image('character.png')

clear_canvas()
boy.draw(400, 300)
update_canvas()

def move_circle():
    print('circle')
    pass

def move_rectangle():
    print('rectangle')
    pass

def move_triangle():
    print('triangle')
    pass

running = True
while running:
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            running = False
            break

    if not running:
        break

    move_circle()
    move_rectangle()
    move_triangle()
    update_canvas()
    delay(0.01)

close_canvas()