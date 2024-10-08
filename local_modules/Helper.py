from math import radians, cos, sin, sqrt


def calculate_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    dist = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist


def rotate_polygon(points, degrees):
    """ Rotate polygon the given angle about its center. """
    # https://stackoverflow.com/a/45511474

    theta = radians(degrees)  # Convert angle to radians
    cos_ang, sin_ang = cos(theta), sin(theta)

    # find center point of Polygon to use as pivot
    n = len(points)
    cx = sum(p[0] for p in points) / n
    cy = sum(p[1] for p in points) / n

    new_points = []
    for p in points:
        x, y = p[0], p[1]
        tx, ty = x-cx, y-cy
        new_x = (tx*cos_ang + ty*sin_ang) + cx
        new_y = (-tx*sin_ang + ty*cos_ang) + cy
        new_points.append((int(new_x), int(new_y)))

    return new_points
