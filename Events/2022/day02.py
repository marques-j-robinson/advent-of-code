from utils import split_by_new_line


shapes = {
	'A': {
		'name': 'rock',
		'score': 1
	},
	'X': {
		'name': 'rock',
		'score': 1
	},
	'B': {
		'name': 'paper',
		'score': 2
	},
	'Y': {
		'name': 'paper',
		'score': 2
	},
	'C': {
		'name': 'scissors',
		'score': 3
	},
	'Z': {
		'name': 'scissors',
		'score': 3
	}
}


class Game:

	def __init__(self, op_move, player_move):
		self.round_score = 0
		self.op_move = shapes[op_move]
		self.player_move = shapes[player_move]

	def score_draw(self):
		self.round_score += 3 + self.player_move['score']

	def score_win(self):
		self.round_score += 6 + self.player_move['score']

	def score_loss(self):
		self.round_score += self.player_move['score']

	def play(self):
		op_move = self.op_move['name']
		player_move = self.player_move['name']
		if op_move == player_move:
			self.score_draw()
		else:
			if op_move == 'rock':
				if player_move == 'paper':
					self.score_win()
				elif player_move == 'scissors':
					self.score_loss()
			if op_move == 'paper':
				if player_move == 'scissors':
					self.score_win()
				elif player_move == 'rock':
					self.score_loss()
			if op_move == 'scissors':
				if player_move == 'rock':
					self.score_win()
				elif player_move == 'paper':
					self.score_loss()


class Solution:

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = [i.split(" ") for i in split_by_new_line(puzzle_input)]

	def solve(self):
		for i in self.data:
			game = Game(i[0], i[1])
			game.play()
			self.p1 += game.round_score