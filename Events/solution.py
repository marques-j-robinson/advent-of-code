import os

import pyperclip

from Events.adventofcode import fetch
from format_string import leading_zero


event = os.getenv('EVENT')
day = leading_zero(os.getenv('DAY'))


def fetch_puzzle_input(puzzle_id):
	cache_path = f'cache/{puzzle_id}'
	if os.path.exists(cache_path):
		f = open(cache_path, 'r')
		res = f.read()
		f.close()
		return res
	else:
		print('---FETCHING PUZZLE INPUT---')
		res = fetch()
		f = open(cache_path, 'w')
		f.write(res)
		f.close()
		return res


class Solution:

	def __init__(self):
		# puzzle input setup
		self.event = event
		self.day = day
		self.id = f'{event}_{day}'
		self.data = fetch_puzzle_input(self.id)
		print(f'puzzle_id:{self.id}')
		# solution setup
		print(f'---SOLVING---')
		self.p1 = 0
		self.p2 = 0

	def copy(self):
	    if self.p2 == 0:
	        pyperclip.copy(str(self.p1))
	    else:
	        pyperclip.copy(str(self.p2))

	def split_by_new_line(self):
		self.data = self.data.split("\n")
