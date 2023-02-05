UP = "("


def step(i):
	if i == UP:
		return 1
	else:
		return -1


def p1(puzzle_input):
	res = 0
	for i in puzzle_input:
		res += step(i)
	return res


def is_basement_entry(floor_id):
	return floor_id == -1


def p2(puzzle_input):
	res = 0	
	floor_id = 0
	for idx, i in enumerate(puzzle_input):
		if res == 0 and is_basement_entry(floor_id):
			res = idx 
		floor_id += step(i)
	return res