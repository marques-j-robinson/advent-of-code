# advent-of-code

## Usage
1) Create and activate a virtual environment
1) Duplicate `.template-env` to `.env` and update GitHub session token
1) Create a `cache` directory
1) Configure `EVENT` and `DAY` values in `.env`
1) Execute `python main.py` to solve the puzzle for the configured values

## Documentation
Notes about specific modules.

### Formatting Data
Any sort of data formatting occurs in this file.
- (Initial Puzzle Input) decoded using UTF-8 and stripped of any new line characters

### Fetching puzzle_input from Advent of Code server
- `python-dotenv` keeps track of an individuals cookie
- `urllib3` make the request to the Advent of Code server
- The response to a successful request is formatted as the initial puzzle input 

### Cache Layer
Before requesting `puzzle_input` there is a check to confirm that the puzzle input can not be found in the `cache` directory.