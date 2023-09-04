import os
import argparse
from dotenv import load_dotenv
load_dotenv()


parser = argparse.ArgumentParser()
parser.add_argument("-e", "--Event", help="Event ID")
parser.add_argument("-d", "--Day", help="Day ID")
args = parser.parse_args()


event = args.Event or os.getenv('EVENT') or 2015
day = args.Day or os.getenv('DAY') or 1
day_with_leading_zero = str(day).zfill(2)
puzzle_id = f'{event}_{day_with_leading_zero}'


if __name__ == "__main__":
    print(puzzle_id)
