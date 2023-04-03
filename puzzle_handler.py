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
url = f'{base_uri}/{event}/day/{day}/input'
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--Event", help="Event ID of puzzle")
parser.add_argument("-y", "--Year", help="(User Friendly) Event ID of puzzle")
parser.add_argument("-d", "--Day", help="Day ID of puzzle")
args = parser.parse_args()


class PuzzleHandler:
	"""
	Cache puzzle input in the file system.

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
		self.e = e
		self.d = d
		self.day_with_leading_zero = leading_zero(d)

	def get_puzzle_input(self):
		"""
		Request puzzle input from the Advent of Code server.
		Minor formatting to the response data:
			- Decoding the String by 'utf-8'
			- Removing any new line characters at the end of the String.
		"""
		http = urllib3.PoolManager()
		r = http.request('GET', url, headers=headers)
		return r.data.decode('utf-8').rstrip('\n')