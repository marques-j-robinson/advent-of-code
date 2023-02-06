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


def differ_by_exactly_one_char(w1, w2):
	if w1 == w2:
		return False
	else:
		diffs = 0
		for idx, i in enumerate(w1):
			j = w2[idx]
			if i != j:
				diffs += 1
		return diffs == 1


def p2(puzzle_input):
	res = ''
	puzzle_input = split_by_new_line(puzzle_input)
	for idx, w1 in enumerate(puzzle_input):
		for w2 in puzzle_input[idx+1:]:
			if differ_by_exactly_one_char(w1, w2) is True:
				for jdx, l in enumerate(w1):
					if l == w2[jdx]:
						res += l
	return res