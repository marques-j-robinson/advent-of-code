from heapq import nsmallest
from lib.file_system import read_input_data

data = read_input_data('2015', 'day02')

def calc_surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def calc_area_sm_side(l, w):
    return l*w

total = 0
for row in data.split('\n'):
    dimensions = [int(i) for i in row.split('x')]
    l, w, h = dimensions
    total+=calc_surface_area(l, w, h)
    l, w = nsmallest(2, dimensions)
    total+=calc_area_sm_side(l, w)
print(f"PART_1: {total} square feet of wrapping paper should be ordered")