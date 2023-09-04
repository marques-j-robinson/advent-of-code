import os
import argparse
import importlib

import urllib3
from dotenv import load_dotenv
load_dotenv()


def get_event_day_by_puzzle_id(puzzle_id):
    return [int(i) for i in puzzle_id.split("_")]


def configure_puzzle_id():
    """
    Use command line arguments first, then look for
    values in the .env file and finally default to
    provided files in this function.
    """
    DEFAULT_EVENT = 2015
    DEFAULT_DAY = 1

    # Command Line Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--Event", help="Event ID")
    parser.add_argument("-d", "--Day", help="Day ID")
    args = parser.parse_args()

    event = args.Event or os.getenv("EVENT") or DEFAULT_EVENT
    day = args.Day or os.getenv("DAY") or DEFAULT_DAY
    day_with_leading_zero = str(day).zfill(2)
    return f"{event}_{day_with_leading_zero}"


# base_url = "https://adventofcode.com"
# puzzle_input_url = f"{base_url}/{event}/day/{day}/input"
# request_headers = {"Cookie":f'session={os.getenv("TOKEN")}'}


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
    puzzle_id = configure_puzzle_id()
    print(f"Executing {puzzle_id} Solution...")
    [event, day] = get_event_day_by_puzzle_id(puzzle_id)
    print(event)
    print(day)
    # puzzle_input = get_puzzle_input()
    # try:
    #     solution_module = importlib.import_module(f"Events.{event}.day{day_with_leading_zero}")
    #     solution = solution_module.Solution(puzzle_input)
    #     print(solution.puzzle_input)
    # except Exception as e:
    #     print("Exception thrown during module import!!")
    #     print(e)
    #     print("Please remember to create the Event folder as well as the solution module and class.")
