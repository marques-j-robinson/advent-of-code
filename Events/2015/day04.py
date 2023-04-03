from itertools import count
from hashlib import md5

from main import CacheLayer


class S(CacheLayer):

	def solve(self):
		for num in count(1):
			test_str = f'{self.puzzle_input}{num}'
			if self.check_test_str(test_str, 5) == '00000':
				self.p1 = num
				break
		for num in count(1):
			test_str = f'{self.puzzle_input}{num}'
			if self.check_test_str(test_str, 6) == '000000':
				self.p2 = num
				break

	def check_test_str(self, test_str, check_value):
		return md5(test_str.encode('utf-8')).hexdigest()[:check_value]