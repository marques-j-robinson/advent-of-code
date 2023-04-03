import hashlib

from main import CacheLayer


class S(CacheLayer):

	def solve(self):
		res = ''
		exit = False
		while exit is False:
			if res[0:5] == '00000':
				exit = True
			else:
				self.p1 += 1
				res = hashlib.md5(f'{self.puzzle_input}{self.p1}'.encode())
				res = res.hexdigest()
