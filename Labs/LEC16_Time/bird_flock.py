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

    def update(self):
        self.x += self.direction * FLIGHT_SPEED * game_framework.frame_time
        left_edge = self.x - 270 - DISPLAY_WIDTH / 2
        right_edge = self.x + 270 + DISPLAY_WIDTH / 2

        if left_edge <= 0:
            self.x = 270 + DISPLAY_WIDTH / 2
            self.direction = 1
        elif right_edge >= get_canvas_width():
            self.x = get_canvas_width() - 270 - DISPLAY_WIDTH / 2
            self.direction = -1

        for bird in self.birds:
            bird.frame = (bird.frame + ANIMATION_FPS *
                          game_framework.frame_time) % FRAME_COUNT

    def draw(self):
        for bird in self.birds:
            frame_index = int(bird.frame)
            row, column = divmod(frame_index, FRAME_COLUMNS)
            source_x = column * FRAME_WIDTH
            source_y = (2 - row) * FRAME_HEIGHT
            flip = '' if self.direction == 1 else 'h'
            self.image.clip_composite_draw(
                source_x, source_y, FRAME_WIDTH, FRAME_HEIGHT,
                0, flip,
                self.x + bird.offset_x, self.y + bird.offset_y,
                DISPLAY_WIDTH, DISPLAY_HEIGHT
            )
