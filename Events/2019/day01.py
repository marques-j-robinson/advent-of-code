from format_data import int_list_by_new_line


def calc_fuel(mass):
	return round(mass//3)-2


def re_calc_fuel(mass, total=0):
	fuel = calc_fuel(mass)
	if fuel <= 0:
		return total
	else:
		total += fuel
	return re_calc_fuel(fuel, total)


def p1(puzzle_input):
	res = 0
	puzzle_input = int_list_by_new_line(puzzle_input)
	for m in puzzle_input:
		res += calc_fuel(m)
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = int_list_by_new_line(puzzle_input)
	for m in puzzle_input:
		res += re_calc_fuel(m)
	return res