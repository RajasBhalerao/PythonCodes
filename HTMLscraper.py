"""Retrieve the last name in a given html link (http://py4e-data.dr-chuck.net/known_by_Nirvana.html)
 by hopping from one link to another. The count of repeat and the at the position of the hop
 is given by client. Repeat the hopping condition up to the count of repeat"""
import urllib.request,urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

scount= input("Enter Count of Repeat:")
count = int(scount)
spos= input("Enter position:")
pos = int(spos)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for i in range(count):
    urllink = tags[pos-1].get('href', None)
    print(tags[pos-1].contents[0], urllink)
    html = urllib.request.urlopen(urllink, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')


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
