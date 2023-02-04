# advent-of-code

## Usage
1) Duplicate `.template-env` to `.env` and update GitHub session token
1) Create a `cache` directory

## Documentation
Notes about specific modules.

### Getting Puzzle Input
- `python-dotenv` keeps track of an individuals cookie
- `urllib3` make the request to the Advent of Code server
- The response to a successful request is decoded using UTF-8 and stripped of any new line characters

### Caching Puzzle Input
Before requesting the puzzle input there is a check to confirm that the puzzle input can not be found in the `cache` directory.