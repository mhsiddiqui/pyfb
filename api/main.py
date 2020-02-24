import requests
import json
import datetime
from collections import namedtuple


class Facebook:

	def __init__(self, APP_ID=None, APP_SECRET=None, VERSION='v6.0', LIMIT=80, JITTER=1.5, DEBUG=False)
		assert APP_ID is not None, "APP_ID is required"
		assert APP_SECRET is not None, "APP_SECRET is required"
		self.APP_ID = APP_ID
		self.APP_SECRET = APP_SECRET
		self.version = VERSION
		self.limit = LIMIT
		self.jitter = JITTER
		self.debug = DEBUG
		self.last_call_time = None
		self.api_usage = {"call_count": 0, "total_time": 0, "total_cputime": 0}

	def _get_url(self):
		pass

	def _objectify(self, data):
		data = {key: val for key, val in d.items()}
	    data['keys'] = list(d.keys())
	    data['values'] = list(d.values())
	    return namedtuple('Object', data.keys())(*data.values())

	def _make_api_call(self):
		self.last_call_time = datetime.datetime.now()
