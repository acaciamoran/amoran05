import math

def distance(point1, point2):
    dist_x = point1.x - point2.x
    dist_y = point1.y - point2.y
    distance = math.sqrt(dist_x ** 2 + dist_y ** 2)
    return distance


def circles_overlap(circle1, circle2, radius1, radius2):
    dist_x = circle1.x - circle2.x
    dist_y = circle1.y - circle2.y
    distance = math.sqrt(dist_x ** 2 + dist_y ** 2)
    sum_radius = radius1 + radius2
    return distance < sum_radius
