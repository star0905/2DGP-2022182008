from pico2d import get_canvas_width, load_image

import game_world


class Ball:
    images = {}

    def __init__(self, x, y, velocity, item_type=1):
        if item_type not in Ball.images:
            image_name = 'ball41x41.png' if item_type == 2 else 'ball21x21.png'
            Ball.images[item_type] = load_image(image_name)
        self.x, self.y = x, y
        self.velocity = velocity
        self.image = Ball.images[item_type]

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
