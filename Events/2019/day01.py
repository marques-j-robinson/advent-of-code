from utils import split_by_new_line, int_list


def calc_fuel(mass):
    return round(mass//3)-2


def re_calc_fuel(mass, total=0):
    fuel = calc_fuel(mass)
    if fuel <= 0:
        return total
    else:
        total += fuel
        return re_calc_fuel(fuel, total)


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = int_list(split_by_new_line(puzzle_input))

	def solve(self):
		for m in self.data:
			self.p1 += calc_fuel(m)
			self.p2 += re_calc_fuel(m)