"""WebScraper for the html (http://py4e-data.dr-chuck.net/comments_1800573.html)
scrape to find the tags which contain number of comments and find the sum of all comments count."""
import urllib.parse,urllib.request, urllib.error
from bs4 import BeautifulSoup

url = input("Enter the URL to be parsed:")
furl = urllib.request.urlopen(url).read()
soup = BeautifulSoup(furl, 'html.parser')
ressum = 0
tags = soup('span')
for tag in tags:
    span = ('Comments:', tag.contents[0])
    comments = int(span[1])
    ressum += comments
print(ressum)
