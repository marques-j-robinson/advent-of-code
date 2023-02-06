from format_data import split_by_new_line
from format_string import get_char_count, remove_diff_chars
from string_validation import differ_by_exactly_one_char


def check_exact(chars, check_val):
	res = False
	for c in chars:
		count = chars[c]
		if check_val == count:
			res = True
	return res


def p1(puzzle_input):
	puzzle_input = split_by_new_line(puzzle_input)
	two = 0
	three = 0
	for word in puzzle_input:
		char_count = get_char_count(word)
		if check_exact(char_count, 2) is True:
			two += 1
		if check_exact(char_count, 3) is True:
			three += 1
	return two*three


def p2(puzzle_input):
	res = ''
	puzzle_input = split_by_new_line(puzzle_input)
	for s1_id, s1 in enumerate(puzzle_input):
		for s2 in puzzle_input[s1_id+1:]:
			if s1 == s2:
				pass
			elif differ_by_exactly_one_char(s1, s2) is True:
				res = remove_diff_chars(s1, s2)
	return res