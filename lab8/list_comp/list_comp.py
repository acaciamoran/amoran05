from funcs_objects import *
from objects import *

def distance_all(points):
    origin = Point(0, 0)
    return [distance(point, origin) for point in points]

def are_in_first_quadrant(points):
    return [point for point in points if point.x >= 0 and point.y >= 0]

