"""The basic outline of this problem is to read the file, look for integers using the re.findall(),
looking for a regular expression of '[0-9]+' and then converting the extracted strings to integers
and summing up the integers."""

import re
lst = list()

ffile = input("Enter the file:")
if len(ffile)<1:
    ffile = "regex_sum_1800571.txt"
fhan = open(ffile)

for words in fhan:
    words.split()
    rewords = re.findall('[0-9]+', words, flags=0)
    if len(rewords)<1:
        continue

    for i in range(len(rewords)):
        nums = int(rewords[i])
        lst.append(nums)

print(sum(lst))



