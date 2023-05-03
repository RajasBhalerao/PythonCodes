"""Assignment 9.4"""
""" Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail 
messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent 
the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number 
of times they appear in the file. After the dictionary is produced, the program reads through the dictionary 
using a maximum loop to find the most prolific committer."""

"""A more refined code is as follows:"""
fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)

count = dict()

for sentence in handle:
    sentence.strip() #initial strip
    words = sentence.split() #splits the words.
    # Weeds/Skips outs any words which are blank.
    if len(words) < 3 or words[0] != 'From':
        continue

# This gives the calculates the total count of the numbers.
    for w in words:
        if w in count:
            count[w] = count[w]+1
        else:
            count[w] = 1

#-1 becuase we are comparing the values with it to determine the max. We are positive that count is greater than 1.
largest = -1
largeword  = None
# .item() is a method which gives key value pairs with 2 iteration variables.
for k,v in count.items():
    # this weeds out any words which do not have '@'.
    if '@' not in k:
        continue
    else:
        # basic max code
        if v > largest:
            largest = v
            largeword = k
print(largeword, largest)


"""Below code works but a more refined code is mentioned above. Below uses mutiple lists and variables to achieve the
results."""
fname = input("Enter file:")
if len(fname) < 1:
    name = "mbox-short.txt"
handle = open(fname)

count = dict()
lst = list()
dummylst = list()
maximum = None
maxemail = None

for sentence in handle:
    sentence.strip()
    words = sentence.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    text = [words[1]]

    dummylst = dummylst + text

for email in dummylst:
    count[email] = count.get(email, 0) + 1
    if maximum is None:
        maximum = count[email]
        maxemail = email
    elif maximum < count[email]:
        maximum = count[email]
        maxemail = email
print(maxemail, maximum)

