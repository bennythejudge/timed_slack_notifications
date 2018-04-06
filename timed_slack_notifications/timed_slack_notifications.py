# main file
import json
from pprint import pprint

JSON_FILE = "timed_slack_notifications.json"

def main():
	# open the json file if it exists
	read_json = json.load(open(JSON_FILE))

	pprint(read_json)
	# read it in memory
	# loop through the content
	# if 
	print("content: {}".format(read_json["content"]))
	print("total entries: {}".format(read_json["total entries"]))

if __name__ == "__main__":
    main()
