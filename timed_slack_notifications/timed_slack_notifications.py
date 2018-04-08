# ----------------------------------------------------------------
# first iteration: 
# - read the file in memory
# - loop through all entries and execute if the time in the entry = current time
# second iteration
# - open file in read mode
# - mark entries executed as such
# - update the file (rewrite it and reread it)
# third iteration
# - use sqllite ? or mysql? or something that can store state?
# --------------------------------------------------------------
# main file
import json
from pprint import pprint
import time
import dateutil.parser as dp
import datetime

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
	while True:
		# this goes into an infinite loop
		for item in items:
			print(item)
			date = item['date']
			entry_time = item['time']
			print("date: {} time: {}".format(date,entry_time))
			# break the entry
			datee = datetime.datetime.strptime(date, "%Y-%m-%d")
			timee = datetime.datetime.strptime(entry_time, "%H:%M:%S")
			print(datee.year)
			print(datee.month)
			print(datee.day)
			print(timee.hour)
			print(timee.minute)
			print(timee.second)
			# now get current time

			# datetime.datetime(2012,4,1,0,0).timestamp()
			# prepare for a cron entry
			# convert timestamp to a one off cron entry
			# prepare the 

if __name__ == "__main__":
    main()
