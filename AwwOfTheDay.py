import requests
import bs4
import webbrowser

response = requests.get('https://www.reddit.com/r/aww/top/.json?t=day&count=5').json()

urls = []

for post in response['data']['children']:
    urls.append(post['data']['url'])

for url in urls:
	webbrowser.open(url)