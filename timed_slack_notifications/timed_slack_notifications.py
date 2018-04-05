# main file
import json


JSON_FILE = "timed_slack_notifications.json"

def main():
	# open the json file if it exists
	with open(JSON_FILE, 'r') as f:
		read_json = json.load(f)
	print(read_json)
	# read it in memory
	# loop through the content
	# if 

if __name__ == "__main__":
    main()
