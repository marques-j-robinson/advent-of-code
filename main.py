import os
import argparse
import importlib

import urllib3
from dotenv import load_dotenv
load_dotenv()


parser = argparse.ArgumentParser()
parser.add_argument("-e", "--Event", help="Event ID")
parser.add_argument("-d", "--Day", help="Day ID")
args = parser.parse_args()


event = args.Event or os.getenv('EVENT') or 2015
day = args.Day or os.getenv('DAY') or 1
day_with_leading_zero = str(day).zfill(2)
puzzle_id = f"{event}_{day_with_leading_zero}"
base_url = "https://adventofcode.com"
puzzle_input_url = f"{base_url}/{event}/day/{day}/input"
request_headers = {"Cookie":f'session={os.getenv("TOKEN")}'}


def get_puzzle_input():
    print("Fetching puzzle input...")
    try:
        http = urllib3.PoolManager()
        response = http.request("GET", puzzle_input_url, headers=request_headers)
        return response.data.decode("utf-8").rstrip("\n")
    except Exception as e:
        print("Exception thrown while fetching puzzle input!!")
        print(e)
        print("Please remember to configure the .env file with a useful TOKEN value.")


if __name__ == "__main__":
    print(f"Executing {puzzle_id} Solution...")
    puzzle_input = get_puzzle_input()
    try:
        solution_module = importlib.import_module(f"Events.{event}.day{day_with_leading_zero}")
        solution = solution_module.Solution(puzzle_input)
        print(solution.puzzle_input)
    except Exception as e:
        print("Exception thrown during module import!!")
        print(e)
        print("Please remember to create the Event folder as well as the solution module and class.")
