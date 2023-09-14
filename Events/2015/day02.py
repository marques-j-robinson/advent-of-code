from utils import split_by_new_line, int_list


class RightRectangularPrism:

	def __init__(self, dimensions):
		self.dimensions = int_list(dimensions.split('x'))
		self.sm_side = self.dimensions[:]
		self.sm_side.remove(max(self.sm_side))

	def calc_surface_area(self):
		[l, w, h] = self.dimensions
		return 2*l*w + 2*w*h + 2*h*l

	def calc_sm_side_area(self):
		res = 1
		for i in self.sm_side:
			res = res * i
		return res

	def calc_sm_side_perimeter(self):
		return sum([2*i for i in self.sm_side])

	def calc_volume(self):
		[l, w, h] = self.dimensions
		return l*w*h


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = split_by_new_line(puzzle_input)

	def solve(self):
		for dimensions in self.data:
			box = RightRectangularPrism(dimensions)
			self.p1 += box.calc_surface_area() + box.calc_sm_side_area()
			self.p2 += box.calc_sm_side_perimeter() + box.calc_volume()