import os
import shutil
import argparse
import importlib

import urllib3
import pyperclip
from dotenv import load_dotenv
load_dotenv()


parser = argparse.ArgumentParser()
parser.add_argument("-e", "--Event", help="Event ID of puzzle")
parser.add_argument("-y", "--Year", help="(User Friendly) Event ID of puzzle")
parser.add_argument("-d", "--Day", help="Day ID of puzzle")
args = parser.parse_args()


class UserInput:

    def __init__(self, e=os.getenv('EVENT'), d=os.getenv('DAY')):
        self.event = args.Event or args.Year or e
        if os.path.exists(f'Events/{self.event}') is False:
            os.mkdir(f'Events/{self.event}')
        self.day = args.Day or d
        self.day_with_leading_zero = str(self.day).zfill(2)
        solution_filepath = f'Events/{self.event}/day{self.day_with_leading_zero}.py'
        if os.path.exists(solution_filepath) is False:
            shutil.copy('template.py', solution_filepath)
        self.id = f'{self.event}_{self.day_with_leading_zero}'
        self.puzzle_input = None
        self.p1 = 0
        self.p2 = 0
        self.solution_module = importlib.import_module(f'Events.{self.event}.day{self.day_with_leading_zero}')


class DataTranslation(UserInput):
    
    def init_puzzle_input(self):
        self.puzzle_input = self.puzzle_input.decode('utf-8').rstrip('\n')
    
    def split_by_new_line(self):
        self.puzzle_input = [i.strip() for i in self.puzzle_input.split("\n")]


class CacheLayer(DataTranslation):
    
    def get_puzzle_input(self):
        if self.is_cached():
            f = open(self.cache_path(), 'r')
            self.puzzle_input = f.read()
            f.close()
        else:
            self.request()
            f = open(self.cache_path(), 'w')
            f.write(self.puzzle_input)
            f.close()

    def cache_path(self):
        return f'cache/{self.id}'

    def is_cached(self):
        return os.path.exists(self.cache_path())

    def set_headers(self):
        return {'Cookie':f"session={os.getenv('TOKEN')}"}

    def set_url(self):
        return f'https://adventofcode.com/{self.event}/day/{self.day}/input'

    def request(self):
        http = urllib3.PoolManager()
        response = http.request('GET', self.set_url(), headers=self.set_headers())
        self.puzzle_input = response.data
        self.init_puzzle_input()


if __name__ == '__main__':
    i = UserInput()
    s = i.solution_module.S()
    s.get_puzzle_input()
    s.solve()
    if s.p2 == 0:
        print(f'Part 1: {s.p1}')
        pyperclip.copy(str(s.p1))
    else:
        print(f'Part 1: {s.p1}')
        print(f'Part 2: {s.p2}')
        pyperclip.copy(str(s.p2))