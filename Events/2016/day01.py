from utils import Grid, split_by_comma, list_of_tuples


up = "N"
down = "S"
left = "W"
right = "E"
directions = [up, down, left, right]
G = Grid(directions)


# Provides context on which direction to proceed with given a starting direction and a turn value
pivot = {
	"NR": "E",
	"NL": "W",
	"SR": "W",
	"SL": "E",
	"ER": "S",
	"EL": "N",
	"WR": "N",
	"WL": "S"
}


class Solution:	

	def __init__(self, puzzle_input):
		self.p1 = 0
		self.p2 = 0
		self.data = list_of_tuples(split_by_comma(puzzle_input))

	def is_intersection(self):
		G.save_coord()
		return self.p2 == 0 and G.coord in G.seen

	def check_intersection(self):
		if self.is_intersection():
			self.p2 = G.manhattan_distance()

	def solve(self):
		direction = up # Starting by facing north
		for turn, steps in self.data:
			direction = pivot[f'{direction}{turn}']
			while steps > 0:
				G.move(direction)
				self.check_intersection()
				G.add_seen()
				steps -= 1
		self.p1 = G.manhattan_distance()