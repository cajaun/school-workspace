import math

def minimum_cubes(height, side, body):
    cubes_per_step = math.ceil(body / side)
    steps = math.ceil(height / side)
    return cubes_per_step * steps * (steps + 1) // 2