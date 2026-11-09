from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.image = load_image('ball21x21.png')

    def update(self):
        self.x += self.direction * 8
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
