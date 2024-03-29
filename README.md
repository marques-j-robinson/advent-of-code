# My aoc Solutions
Solutions to [aoc](https://adventofcode.com/).

## Setup
- clone repo
- Create Virtial Environment: `python -m venv venv && source venv/bin/activate`
- Install Dependencies:
  - Python `pip install --upgrade pip && pip install -r requirements.txt`
  - JavaScript (NodeJs) `npm install`
- Create settings configuration file `touch .env`

**Tip** Recieving permission denied error while piping stored puzzle input file to node script? Following these for [basic chmod usage](https://stackoverflow.com/a/48757287) and [-R flag usage](https://stackoverflow.com/a/11512211)

```bash
sudo chmod -R 755 cache/
```

## Download Puzzle Input
Python script that stores puzzle input files to the filesystem.

Input file may be found here: `/cache/{year}/{day}`

**Notes**
- Ensure virtual environment is active and dependencies installed
- *year* and *day* are configurable within `.env`
- Bypasses if input file already exists in the cache

```bash
python download.py
```

## JavaScript
Leveraging [Nodemon's ability to execute multiple commands](https://github.com/remy/nodemon/issues/1239#issuecomment-533034562) and [npm script command line arguments](https://stackoverflow.com/a/25356509).
### Solve Script
Solution JavaScript code will be found here: `/js/{event}/{day}.js`

```bash
AOC=2015/1 npm run solve
```

### TEST Script
Helpful workaround for passing in custom test data instead of live puzzle input datafile.

Create `/cache/test` file and store anything here to be read during test script execution.

```bash
AOC=2015/1 npm run test
```
