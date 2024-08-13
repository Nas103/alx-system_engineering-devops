#!/usr/bin/python3
import requests

def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code == 200:
        data = response.json()
        after = data.get('data', {}).get('after')
        posts = data.get('data', {}).get('children', [])
        
        for post in posts:
            hot_list.append(post.get('data', {}).get('title'))
        
        if after is not None:
            return count_words(subreddit, word_list, hot_list, after)
        else:
            count_dict = {}
            for word in word_list:
                count_dict[word.lower()] = 0
            
            for title in hot_list:
                title_words = title.lower().split()
                for word in word_list:
                    word_lower = word.lower()
                    count_dict[word_lower] += title_words.count(word_lower)
            
            count_dict = {k: v for k, v in count_dict.items() if v > 0}
            sorted_words = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
            
            for word, count in sorted_words:
                print("{}: {}".format(word, count))
    else:
        return None
