import requests 
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res.text, 'html.parser')

votes = soup.select('.score')

links = soup.select('.storylink')
links2 = soup.select('.storylink')

subtext = soup.select('.subtext')
subtext2 = soup.select('.subtext')

mega_subtext = subtext + subtext2
mega_links = links + links2

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k: k['votes'], reverse = True)

def  create_custom_hn(links, subtext):
	hn = []
	for idx, items in enumerate(links):
		title = links[idx].getText()
		href = links[idx].get('href', None)
		votes = subtext[idx].select('.score')
		if len(votes):
			points = int(votes[0].getText().replace('points', " "))
			if points > 99:hn.append({ 'votes': points, 'Title' : title, 'Links': href,})
	return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))