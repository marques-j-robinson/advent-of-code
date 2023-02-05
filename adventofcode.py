import os
import urllib3
from format_data import init_format


def setup_url():
	base = 'https://adventofcode.com'	
	event = os.getenv('EVENT')
	day = os.getenv('DAY')
	return f'{base}/{event}/day/{day}/input'


def setup_request_headers():
	session = os.getenv('GITHUB')
	return {'Cookie':f'session={session}'}


def fetch():
	print('Fetching puzzle_input from server...')
	http = urllib3.PoolManager()
	r = http.request('GET', setup_url(), headers=setup_request_headers())
	return init_format(r.data)