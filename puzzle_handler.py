import os
import argparse
import urllib3

from dotenv import load_dotenv
load_dotenv()

from format_string import leading_zero


event = os.getenv('EVENT')
day = os.getenv('DAY')
headers = {'Cookie'f'session={os.getenv('TOKEN')}'}
base_uri = 'https://adventofcode.com'
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--Event", help="Event ID of puzzle")
parser.add_argument("-y", "--Year", help="(User Friendly) Event ID of puzzle")
parser.add_argument("-d", "--Day", help="Day ID of puzzle")
args = parser.parse_args()


class PuzzleHandler:
	"""
	Import puzzle solution module.
	Execute solve function.
	At this point, the solution module will handle the rest of the requirements for solving the puzzle.
	"""

	def __init__(self, e=event, d=day):
		"""
		Understand Event/Year and Day values provided by the user.
		This can be done a few ways:
			- Hard coding the values in the filesystem
				(either in python files or through dotfiles configuring the programs environment)
			- Accept arguments from the command line prompt
		"""
		e = args.Event or args.Year or e
		d = args.Day or d
		self.url = f'{base_uri}/{e}/day/{d}/input'
		self.e = e
		self.d = d
		self.day_with_leading_zero = leading_zero(d)
		self.id = f'{e}_{self.day_with_leading_zero}'
		self.data = self.cached_puzzle_input()

	def get_puzzle_input(self):
		"""
		Request puzzle input from the Advent of Code server.
		Minor formatting to the response data:
			- Decoding the String by 'utf-8'
			- Removing any new line characters at the end of the String.
		"""
		http = urllib3.PoolManager()
		r = http.request('GET', self.url, headers=headers)
		return r.data.decode('utf-8').rstrip('\n')

	def cached_puzzle_input(self):
		"""
		Cache puzzle input in the file system.
		Check cache/ directory for existing puzzle file.
		Otherwise, request puzzle input from the server and save the response to the cache/ directory.
		"""
		cache_path = f'cache/{self.id}'
		if os.path.exists(cache_path):
			f = open(cache_path, 'r')
			res = f.read()
			f.close()
			return res
		else:
			res = self.get_puzzle_input()
			f = open(cache_path, 'w')
			f.write(res)
			f.close()
			return res
