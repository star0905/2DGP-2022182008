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
        self.birds = self._create_birds()

    @staticmethod
    def _create_birds():
        formation = (
            (-270, 35), (-180, 85), (-90, 45), (0, 100), (90, 55),
            (180, 90), (270, 35), (-135, -35), (45, -20), (180, -45),
        )
        return [
            Bird(offset_x, offset_y, index * 1.4 % FRAME_COUNT)
            for index, (offset_x, offset_y) in enumerate(formation[:BIRD_COUNT])
        ]
