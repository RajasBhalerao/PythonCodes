"""Chapter 8-4"""

"""Open the file romeo.txt and read it line by line. For each line, split the line into a list of words
using the split() method. The program should build a list of words. For each word on each line check to
see if the word is already in the list and if not append it to the list. When the program completes, sort
and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt"""

fname = input("Enter file name: ") #Add the desired text file to this variable.
fh = open(fname)

"""We create 3 lists:  1 orignal which contains all the text, TargetLst to split the text, 
FLst to identify the unqiue items."""
lst = list()
TargetLst = list()
FLst = list()


"""For loop to iterate through the list and append the indivisual lines to lst (orginal) list followed by 
stripping white spaces and spliting indivisual words in the Target list"""
for line in fh:
    lst.append(line)
    line.strip()
    for words in line:
        TargetLst += line.split()

"""To compare 2 lists and find the missing items in one list we use the set() and update().
This entails us to create 2 new variables and use the above functions."""
listT_set = set(TargetLst)
listF_set = set(FLst)
listF_set.update(listT_set)
FLst = list(listF_set)
FLst.sort()

#Print
print(FLst)

