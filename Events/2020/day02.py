import re
from format_data import split_by_new_line


regex = r"(\d*-\d*) ([a-zA-Z]): ([a-zA-Z]*)([a-zA-Z]*)"


def parse_instructions(i):
	res = re.match(regex, i)
	[freq_min, freq_max] = [int(i) for i in res.group(1).split("-")]
	return [freq_min, freq_max, res.group(2), res.group(3)]


def format_puzzle_input(puzzle_input):
	return [parse_instructions(i) for i in split_by_new_line(puzzle_input)]


def get_letter_count(password, letter):
	count = 0
	for l in password:
		if letter == l:
			count += 1
	return count


def p1(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for p in puzzle_input:
		[freq_min, freq_max, letter, password] = p
		count = get_letter_count(password, letter)
		if freq_min <= count and freq_max >= count:
			res += 1
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for p in puzzle_input:
		[a_idx, b_idx, letter, password] = p
		if (password[a_idx-1] == letter) ^ (password[b_idx-1] == letter):
			res += 1
	return res