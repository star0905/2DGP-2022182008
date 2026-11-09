from pico2d import *
from ball import Ball
from boy import Boy
from grass import Grass
import game_world


def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            direction = boy.handle_event(event)
            if direction is not None:
                direction_name = '오른쪽' if direction == 1 else '왼쪽'
                print(f'볼 발사 방향: {direction_name}')
                ball = Ball(boy.x + direction * 45, boy.y, direction)
                game_world.add_object(ball, 1)



def reset_world():
    global boy

    left_grass = Grass(50)
    game_world.add_object(left_grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    right_grass = Grass(80)
    game_world.add_object(right_grass, 2)


def update_world():
    game_world.update()
    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()
    pass


running = True

open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
