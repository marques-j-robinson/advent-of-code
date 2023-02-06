def manhattan_distance(a, b):
    return abs(a) + abs(b)


def surface_area(n):
    [x, y, z] = n
    return 2*x*y + 2*x*z + 2*y*z


def area(n):
    res = 1
    for i in n:
        res = res * i
    return res


def perimeter(n):
    return sum([2*i for i in n])


def volume(n):
    [x, y, z] = n
    return x*y*z