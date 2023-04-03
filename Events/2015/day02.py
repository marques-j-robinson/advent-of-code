from main import CacheLayer, int_list


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


class S(CacheLayer):

	def solve(self):
		self.split_by_new_line()
		for dimensions in self.puzzle_input:
			self.box(dimensions)
			self.p1 += surface_area(self.sides) + area(self.sm_side)
			self.p2 += volume(self.sides) + perimeter(self.sm_side)

	def box(self, dimensions):
		self.sides = int_list(dimensions.split('x'))
		self.sm_side = self.sides[:]
		self.sm_side.remove(max(self.sm_side))