from format_data import split_by_new_line, int_list


def format_puzzle_input(puzzle_input):
	return int_list(split_by_new_line(puzzle_input))


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
	puzzle_input = format_puzzle_input(puzzle_input)
	for m in puzzle_input:
		res += calc_fuel(m)
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for m in puzzle_input:
		res += re_calc_fuel(m)
	return res