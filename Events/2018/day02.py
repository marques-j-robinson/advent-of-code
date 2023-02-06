from format_data import split_by_new_line


def char_count(word):
	chars = {}
	for l in word:
		if l not in chars.keys():
			chars[l] = 1
		else:
			chars[l] += 1
	return chars


def check_exact(chars, check):
	res = False
	for c in chars:
		val = chars[c]
		if val == check:
			res = True
	return res


def p1(puzzle_input):
	puzzle_input = split_by_new_line(puzzle_input)
	two = 0
	three = 0
	for word in puzzle_input:
		chars = char_count(word)
		if check_exact(chars, 2) is True:
			two += 1
		if check_exact(chars, 3) is True:
			three += 1
	return two*three


def p2(puzzle_input):
	res = 0
	puzzle_input = split_by_new_line(puzzle_input)
	return res