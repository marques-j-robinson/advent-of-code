from format_data import split_by_new_line
from shape import Cube
from calc import surface_area, area, volume, perimeter


def p1(puzzle_input):
	res = 0
	puzzle_input = split_by_new_line(puzzle_input)
	for i in puzzle_input:
		box = Cube(i)
		res += surface_area(box.sides) + area(box.sm_side)
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = split_by_new_line(puzzle_input)
	for i in puzzle_input:
		box = Cube(i)
		res += volume(box.sides) + perimeter(box.sm_side)
	return res