from pico2d import draw_rectangle


world = [[], [], []]  # 0: 배경, 1: 오브젝트, 2: UI
DEBUG_DRAW_BB = True

def add_object(o, depth=1):
    world[depth].append(o)


def add_oject(o, depth=1):
    add_object(o, depth)


def add_objects(ol, depth=1):
    world[depth] += ol

def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()
            if DEBUG_DRAW_BB and hasattr(o, 'get_bb'):
                draw_rectangle(*o.get_bb())

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

collision_pairs = {}

collision_pairs = {}
def add_collision_pair(group, a, b):
 if group not in collision_pairs:
     print(f'Added new group {group}')
 collision_pairs[group] = [ [], [] ]
 if a:
     collision_pairs[group][0].append(a)
 if b:
    collision_pairs[group][1].append(b)

def handle_collision():
    for group, pairs in collision_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                if collide(a, b):
                    a.handle_collision(b)
                    b.handle_collision(a)

def clear():
    for layer in world:
        layer.clear()
