from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
DISPLAY_HEIGHT = CANVAS_HEIGHT // 2
FRAME_INTERVAL = 0.08
REPETITIONS_PER_ACTION = 5
ACTION_PAUSE = 1.0
IMAGE_PATH = Path(__file__).resolve().parent / "sonic-sprite.png"
ANIMATION_REGIONS = (
    ("동작 01", 0, 38, 335, 41),
    ("동작 02", 0, 78, 399, 40),
    ("동작 03", 0, 120, 262, 45),
    ("동작 04", 0, 166, 299, 35),
    ("동작 05", 0, 205, 218, 30),
    ("동작 06", 0, 237, 218, 38),
    ("동작 07", 0, 282, 258, 39),
    ("동작 08", 0, 325, 172, 48),
    ("동작 09", 180, 325, 95, 48),
    ("동작 10", 0, 376, 288, 42),
    ("동작 11", 0, 425, 150, 45),
)
ANIMATION_FRAME_COUNTS = (11, 13, 6, 9, 6, 6, 6, 6, 2, 8, 4)


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