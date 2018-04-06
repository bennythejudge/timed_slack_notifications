# main file
import json
from pprint import pprint
import time
import dateutil.parser as dp

JSON_FILE = "timed_slack_notifications.json"

def main():
	# time now
	ts = int(time.time())
	print("ts: {}".format(ts))

	# open the json file if it exists
	read_json = json.load(open(JSON_FILE))

	# pprint(read_json)
	# read it in memory
	# loop through the content
	# if 
	# print("content: {}".format(read_json["content"]))
	# print("total entries: {}".format(read_json["total entries"]))
	items = read_json["items"]
	# print("items: {}".format(items))
	for item in items:
		print(item)
		entry_ts = item['timestamp']
		print("entry_ts: {}".format(entry_ts))

if __name__ == "__main__":
    main()
