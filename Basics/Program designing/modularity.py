import math


def distance(delta_x, delta_y):
    """
    :param delta_x: (float) the defence between x-coordinator
    :param delta_y: (float) the defence between x-coordinator
    :return: (float) the distance between two points
    """
    distance = math.sqrt(delta_x ** 2 + delta_y ** 2)
    return distance


def slope(delta_x, delta_y):
    """
    :param delta_x: (float) the defence between x-coordinator
    :param delta_y: (float) the defence between y-coordinator
    :return: (float) slope between two points
    """
    slope = (delta_y) / (delta_x)
    return slope


def intercept(x1, y1, slope):
    """
    :param x1: (float) x-intercept for first  point
    :param y1: (float) y-intercept for first  point
    :param slope: (float) the slope
    :return: (float) y-intercept of the line connecting the two points
    """
    return y1 - slope * x1


if __name__ == '__main__':
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    delta_x = x2 - x1
    delta_y = y2 - y1
    print(f"Distance: {distance(delta_x, delta_y)}")
    print(f"Slope: {slope(delta_x, delta_y)}")
    print(f"Y-intercept: {intercept(x1, y1, slope(delta_x, delta_y))}")
