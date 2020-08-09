import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
res3 = requests.get('https://news.ycombinator.com/news?p=3')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
soup3 = BeautifulSoup(res3.text, 'html.parser')
# print(soup.body.contents)
# print(soup.find_all('a')) #to access different data from websites
# print(soup.find_all('div'))
links = soup.select('.storylink')
subtext = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')
links3 = soup3.select('.storylink')
subtext3 = soup3.select('.subtext')
mega_links = links + links2 + links3
mega_subtext = subtext + subtext2 + subtext3
# print(soup.find_all(id='score_23910512'))
# print(votes[0])


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def custom_hn(links, subtext):
    hn = []
    for idx, items in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})

    return sort_stories_by_votes(hn)


pprint.pprint(custom_hn(mega_links, mega_subtext))
