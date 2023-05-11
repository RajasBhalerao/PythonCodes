"""The main motive is to traverse down a xml file and calculate the sum of numbers which
are assigned to each child by the 'count' field"""

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup

total = 0
inputUrl = input("Enter the url:")

# Opening and reading input xml data
html = urllib.request.urlopen(inputUrl).read()
print('Recieved', len(html), 'characters')

# Parses an XML section from a string constant
tree = ET.fromstring(html)

# Now we traverse down the tree to find the comment(child).
counts = tree.findall('comments/comment')

# We can how iterate through indivisual line of child
for x in counts:
    # Now we just go down and find 'count' of each child and convert it to text
    val = x.find('count').text
    total = total + int(val)
print(total)


"""
You can also find the counts using beautifulsoup

soup = BeautifulSoup(html, features="xml")
tags = soup('count')
for tag in tags:
    print(tag)"""

