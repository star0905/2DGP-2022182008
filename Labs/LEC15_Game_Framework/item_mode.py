import game_world
from pico2d import *


image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def update():
    pass


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            import game_framework
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            import game_framework
            game_framework.pop_mode()
