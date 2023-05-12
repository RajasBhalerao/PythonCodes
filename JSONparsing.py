"""In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract
the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
We provide two files for this assignment. One is a sample file where we give you the sum for your testing and
the other is the actual data you need to process for the assignment.

Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
Actual data: http://py4e-data.dr-chuck.net/comments_1800576.json (Sum ends with 44)"""

import json
import urllib.error, urllib.request, urllib.parse

res = 0

url = input("Enter the url of the JSON:")
html = urllib.request.urlopen(url).read()
print("Number of elements is:", len(html))

""".load() load from string. USed for parcing and error handling
The data turns into a dict{} """

info = json.loads(html)

for items in info['comments']:
    count = items['count']
    res = res + int(count)

print(res)



