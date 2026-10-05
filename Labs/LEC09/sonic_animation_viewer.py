from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    running = True

    while running:
        for event in get_events():
            if event.type == SDL_QUIT or (
                event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
            ):
                running = False
                break

        clear_canvas()
        update_canvas()
        delay(0.01)

    close_canvas()


if __name__ == "__main__":
    main()