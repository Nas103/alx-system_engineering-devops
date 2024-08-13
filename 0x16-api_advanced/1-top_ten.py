#!/bin/usr/python3

"""
prints top ten hot posts
"""
import requests

def top_ten(subreddit):
	url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
	headers = {
		 "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
	}
	params = {
	"limit": 10
	}
	response = requests.git(url, headers=headers, params=params, allow_redirects=False)
	if response.status_code == 404:
		print("None")
		return
			results = response.json().get("data")

	[print(c.get("data").get("title")) for c in results.get("children")]
