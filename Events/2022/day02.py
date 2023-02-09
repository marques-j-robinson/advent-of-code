from format_data import split_by_new_line


symbol_scores = {
	"rock": 1,
	"paper": 2,
	"scissors": 3
}


outcomes = {
	"X": "lose",
	"Y": "draw",
	"Z": "win"
}


def format_puzzle_input(puzzle_input):
	return [i.split(' ') for i in split_by_new_line(puzzle_input)]


def translate_symbol(i, outcome=False):
	if i == "A" or i == "X":
		if outcome is True:
			return outcomes["X"]
		return "rock"
	elif i == "B" or i == "Y":
		if outcome is True:
			return outcomes["Y"]
		return "paper"
	elif i == "C" or i == "Z":
		if outcome is True:
			return outcomes["Z"]
		return "scissors"


def play_game(a, b):
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
	for symbols in puzzle_input:
		a = translate_symbol(symbols[1])
		b = translate_symbol(symbols[0])
		res += play_game(a, b) + symbol_scores.get(a)
	return res


def calc_move_per_outcome(outcome, move):
	if outcome == "draw":
		return move
	elif outcome == "lose":
		if move == "rock":
			return "scissors"
		elif move == "scissors":
			return "paper"
		elif move == "paper":
			return "rock"
	elif outcome == "win":
		if move == "rock":
			return "paper"
		elif move == "paper":
			return "scissors"
		elif move == "scissors":
			return "rock"


def p2(puzzle_input):
	res = 0
	puzzle_input = format_puzzle_input(puzzle_input)
	for symbols in puzzle_input:
		outcome = translate_symbol(symbols[1], outcome=True)
		b = translate_symbol(symbols[0])
		a = calc_move_per_outcome(outcome, b)
		res += play_game(a, b) + symbol_scores.get(a)
	return res