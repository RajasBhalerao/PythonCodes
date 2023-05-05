"""Write a program to read through the mbox-short.txt and figure out the distribution by hour of the
day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and
then splitting the string a second time using a colon. From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
 Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below."""

#Input files
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

dic = dict()
for sentence in handle:
    sentence.strip()
    words = sentence.split()
    #Expectioning any sentences which are either null, less than 3 or which do not start with From.
    if len(words)<3 or words[0] != 'From':
        continue
    #print("word:", words)
    #Selecting just the time part for the sentence
    htime = words[5]
    #print("way way before:", htime)
    #splitting the time part into hr,min,sec using ":" as the seperator
    hour = htime.split(":")
    #print("way before:", hour)
    #Selecting just the hour part.
    hour = str(hour[:1])
    #print("before:",hour)
    #selecting just the numbers and discarding the brackerts [] and quotes ''
    hour = hour[2:4]
    #print("after:",hour)
    #Counting the number of time the number repeates and updates the time and count to the dictionary
    if hour in dic:
        dic[hour] = dic[hour] +1
    else:
        dic.update({hour:1})


#Converting the dic into list/tuple
lst = list()
for a, b in dic.items():
    tup = (a,b)
    lst.append(tup)
    print("tup",tup)

#sorting the answer
for x, y in sorted(lst):
    print(x,y)