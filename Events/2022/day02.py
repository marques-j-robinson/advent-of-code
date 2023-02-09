from format_data import split_by_new_line


scores = {
	"rock": 1,
	"paper": 2,
	"scissors": 3
}


def format_puzzle_input(puzzle_input):
	return [i.split(' ') for i in split_by_new_line(puzzle_input)]


def translate_move(i):
	if i == "A" or i == "X":
		return "rock"
	elif i == "B" or i == "Y":
		return "paper"
	elif i == "C" or i == "Z":
		return "scissors"


def rock_paper_scissors(a, b):
	if a == b:
		return 3
	if a == 'paper' and b == 'rock':
		return 6
	elif a == 'rock' and b == 'scissors':
		return 6
	elif a == 'scissors' and b == 'paper':
		return 6
	else:
		return 0


def p1(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for moves in puzzle_input:
		a = translate_move(moves[1])
		b = translate_move(moves[0])
		res += rock_paper_scissors(a, b) + scores.get(a)
	return res


def p2(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	return res