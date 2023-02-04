import os

from dotenv import load_dotenv
load_dotenv()


def setup_request_headers():
	session = os.getenv('GITHUB')
	return {'Cookie':f'session={session}'}