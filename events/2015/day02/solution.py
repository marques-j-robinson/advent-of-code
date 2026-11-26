from heapq import nsmallest
from lib.file_system import read_input_data

data = read_input_data('2015', 'day02')

def calc_surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def calc_area_sm_side(l, w):
    return l*w

def calc_perimeter_sm_side(l, w):
    return l*2+w*2

def calc_volume(l, w, h):
    return l*w*h

p1_total = 0
p2_total = 0
for row in data.split('\n'):
    dimensions = [int(i) for i in row.split('x')]
    l, w, h = dimensions
    p1_total+=calc_surface_area(l, w, h)
    p2_total+=calc_volume(l, w, h)
    l, w = nsmallest(2, dimensions)
    p1_total+=calc_area_sm_side(l, w)
    p2_total+=calc_perimeter_sm_side(l, w)
print(f"PART_1: {p1_total} square feet of wrapping paper should be ordered")
print(f"PART_2: {p2_total} feet of ribbon should be ordered")