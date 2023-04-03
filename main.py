import os
import argparse
import importlib

import urllib3
import pyperclip
from dotenv import load_dotenv
load_dotenv()


class Config:
    
    def __init__(self, e=os.getenv('EVENT'), d=os.getenv('DAY')):
        args = self.argparse_init()
        self.event = args.Event or args.Year or e
        self.day = args.Day or d
        self.day_with_leading_zero = str(self.day).zfill(2)
        self.id = f'{self.event}_{self.day_with_leading_zero}'
        self.p1 = 0
        self.p2 = 0

    def part1(self):
        pass

    def part2(self):
        pass

    def puzzle_input_url(self):
        return f'https://adventofcode.com/{self.event}/day/{self.day}/input'

    def cache_path(self):
        return f'cache/{self.id}'

    def is_cached(self):
        return os.path.exists(self.cache_path())

    def import_solution_module(self):
        return importlib.import_module(f'Events.{self.event}.day{self.day_with_leading_zero}')

    def argparse_init(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("-e", "--Event", help="Event ID of puzzle")
        parser.add_argument("-y", "--Year", help="(User Friendly) Event ID of puzzle")
        parser.add_argument("-d", "--Day", help="Day ID of puzzle")
        return parser.parse_args()


class DataTranslation(Config):
    
    def format_puzzle_input(self):
        self.puzzle_input = self.puzzle_input.decode('utf-8').rstrip('\n')
    
    def split_by_new_line(self):
        self.puzzle_input = [i.strip() for i in self.puzzle_input.split("\n")]


class Http(DataTranslation):
    
    def set_headers(self):
        return {'Cookie':f"session={os.getenv('TOKEN')}"}

    def request(self):
        http = urllib3.PoolManager()
        response = http.request('GET', self.puzzle_input_url(), self.set_headers())
        self.format_puzzle_input(response.data)


class FileSystem(Http):

    def cache_layer(self):
        if self.is_cached():
            f = open(self.cache_path(), 'r')
            self.puzzle_input = f.read()
            f.close()
        else:
            self.request()
            f = open(self.cache_path(), 'w')
            f.write(self.puzzle_input)
            f.close()


class PuzzleHarness(FileSystem):

    def solve(self):
        self.cache_layer()
        self.p1 = self.part1()
        self.p2 = self.part2()
        self.print_and_copy()

    def print_and_copy(self):
        if self.p2 == 0:
            print(f'Part 1: {self.p1}')
            pyperclip.copy(str(self.p1))
        else:
            print(f'Part 1: {self.p1}')
            print(f'Part 2: {self.p2}')
            pyperclip.copy(str(self.p2))

if __name__ == '__main__':
    config = PuzzleHarness()
