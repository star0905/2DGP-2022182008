import game_framework
import game_world
from pico2d import *


image = None
selected_item = None
display_started_at = 0.0


def init():
    global image, display_started_at
    image = load_image('item_select.png')
    display_started_at = get_time()
    if selected_item is not None:
        import playname
        playname.boy.item_type = selected_item


def finish():
    global image, selected_item
    del image
    selected_item = None


def update():
    if selected_item is not None and get_time() - display_started_at >= 0.5:
        game_framework.pop_mode()


def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()


def handle_events():
    global selected_item

    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
        elif event.type == SDL_KEYDOWN and event.key in (SDLK_0, SDLK_1, SDLK_2):
            import playname
            selected_item = event.key - SDLK_0
            playname.boy.item_type = selected_item
            if selected_item is not None:
                game_framework.pop_mode()
