from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
DISPLAY_HEIGHT = CANVAS_HEIGHT // 2
FRAME_INTERVAL = 0.08
REPETITIONS_PER_ACTION = 5
ACTION_PAUSE = 1.0


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (
            event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
        ):
            return False
    return True


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    running = True

    while running:
        running = handle_events()
        clear_canvas()
        update_canvas()
        delay(0.01)

    close_canvas()


if __name__ == "__main__":
    main()