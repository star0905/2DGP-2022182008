from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
DISPLAY_HEIGHT = CANVAS_HEIGHT // 2
FRAME_INTERVAL = 0.08
REPETITIONS_PER_ACTION = 5
ACTION_PAUSE = 1.0
IMAGE_PATH = Path(__file__).resolve().parent / "sonic-sprite.png"


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (
            event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE
        ):
            return False
    return True


def load_sprite():
    if not IMAGE_PATH.is_file():
        raise FileNotFoundError(f"스프라이트 파일을 찾을 수 없습니다: {IMAGE_PATH}")

    try:
        return load_image(str(IMAGE_PATH))
    except Exception as error:
        raise RuntimeError(f"스프라이트 파일을 불러올 수 없습니다: {IMAGE_PATH}") from error


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite = load_sprite()
    except (FileNotFoundError, RuntimeError) as error:
        print(error)
        close_canvas()
        return

    running = True

    while running:
        running = handle_events()
        clear_canvas()
        update_canvas()
        delay(0.01)

    close_canvas()


if __name__ == "__main__":
    main()