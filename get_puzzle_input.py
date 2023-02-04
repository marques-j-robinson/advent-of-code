import os
import urllib3
from dotenv import load_dotenv
load_dotenv()


def setup_url(event, day):
	base = 'https://adventofcode.com'	
	return f'{base}/{event}/day/{day}/input'


def setup_request_headers():
	session = os.getenv('GITHUB')
	return {'Cookie':f'session={session}'}


def format_init_puzzle_input(data):
	return data.decode('utf-8').rstrip('\n')


def get_puzzle_input(event, day):
	http = urllib3.PoolManager()
	r = http.request('GET', setup_url(event, day), headers=setup_request_headers())
	return format_init_puzzle_input(r.data)