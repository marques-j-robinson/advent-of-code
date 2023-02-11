def int_list(a):
    return [int(i) for i in a]


def is_even(i):
    return i % 2 == 0


def combine(a, b):
    return len(a + list(set(b) - set(a)))


def manhattan_distance(a, b):
    return abs(a) + abs(b)
