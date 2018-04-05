# make sure the json file exists
import unittest
import os.path

JSON_FILE = "timed_slack_notifications.json"

class TddJSONFile(unittest.TestCase):

	def test_JSON_file_exists(self):
		assert os.path.isfile(JSON_FILE)
