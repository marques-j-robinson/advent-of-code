import os
import urllib3


def setup_url():
	base = 'https://adventofcode.com'	
	event = os.getenv('EVENT')
	day = os.getenv('DAY')
	return f'{base}/{event}/day/{day}/input'


def setup_request_headers():
	session = os.getenv('GITHUB')
	return {'Cookie':f'session={session}'}


def format_init_puzzle_input(data):
	return data.decode('utf-8').rstrip('\n')


def get_puzzle_input():
	http = urllib3.PoolManager()
	r = http.request('GET', setup_url(event, day), headers=setup_request_headers())
	return format_init_puzzle_input(r.data)