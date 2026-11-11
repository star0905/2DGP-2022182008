from pico2d import *
import game_world
import game_framework
from bird_flock import BirdFlock
from grass import Grass

bird_flock = None


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def init():
    global bird_flock

    bird_flock = BirdFlock()
    game_world.add_oject(bird_flock)

    grass = Grass()
    game_world.add_oject(grass, 0)


def pause():
    pass


def resume():
    pass


def finish():
    global bird_flock
    game_world.clear()
    bird_flock = None


def update():
    game_world.update()

def render():
    clear_canvas()
    game_world.render()
    update_canvas()








