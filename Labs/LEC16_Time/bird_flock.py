from dataclasses import dataclass

from pico2d import get_canvas_width, load_image

import game_framework


FRAME_WIDTH = 183
FRAME_HEIGHT = 168
FRAME_COLUMNS = 5
FRAME_COUNT = 14
BIRD_COUNT = 10
ANIMATION_FPS = 12.0
FLIGHT_SPEED = 180.0
DISPLAY_WIDTH = 110
DISPLAY_HEIGHT = 101


@dataclass
class Bird:
    offset_x: float
    offset_y: float
    frame: float


class BirdFlock:
    def __init__(self):
        self.image = load_image('bird_animation.png')
        self.x = 150.0
        self.y = 410.0
        self.direction = 1
