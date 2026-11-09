world = [[], [], []]  # layers for game objects


def add_object(o, depth):
    world[depth].append(o)


def remove_object(o):
    for layer_index, layer in enumerate(world):
        if o in layer:
            world[layer_index].remove(o)
            return

    raise ValueError("Object not found")


def update():
    for layer in world:
        for o in list(layer):
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()