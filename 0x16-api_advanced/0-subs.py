i!/usr/bin/python3
"""
Queries subscribers on reddit subreddit.
"""
import requests

def number_of_subcribers(subreddit):
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {"User-Agent": "Mozilla/5.0"}
	response = requests.get(url, headers=headers, allow_redirects=False)
	if response.staus_code == 200:
		data = response.json()
		subscribers = data['data']['subscribers']
		return subscribers
	else:
		return 0
