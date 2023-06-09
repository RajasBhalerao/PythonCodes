"""Replace each special symbol with # in the following string"""
import string
str1 = '/*Jon is @developer & musician!!'

for i in string.punctuation:
    str1 = str1.replace(i,'#')

print(str1)

"""Removal all characters from a string except integers"""
import re
str1 = 'I am 25 years and 10 months old'
resu =""
res = re.findall("[0-9]+?",str1)

for i in res:
    resu += i
print(resu)



"""Remove special symbols / punctuation from a string"""
import re
str1 = "/*Jon is @developer & musician"

res = re.sub([A-Za-z], str1)
print("New string is", res)"""

""" Remove empty strings from a list of strings"""
"""str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res = list()
for i in str_list:
    if i == "" or i is None:
        continue
    else:
        res.append(i)
print(res)


""" Split a string on hyphens"""
str1 = "Emma-is-a-data-scientist"

words = str1.split("-")

for i in words:
    print(i)

""" Count all letters, digits, and special symbols from a given string"""
import re

def LDSS(str1):
    Chars = 0
    Digits = 0
    Symbols = 0
    for i in str1:
        if i.isalpha():
            Chars +=1
        elif i.isdigit():
            Digits +=1
        else:
            Symbols +=1
    print("Chars =", Chars,
          "Digits =", Digits,
          "Symbols =", Symbols)
LDSS("P@#yn26at^&i5ve")

"""Arrange string characters such that lowercase letters should come first"""
import re

def LU(str1):
    lower = re.findall("[a-z]+", str1)
    upper = re.findall("[A-Z]+", str1)
    res = lower+upper
    sres = ""
    for i in res:
        sres += i
    print(sres)
LU("JuLiaWillS")


"""Create a new string made of the first, middle, and last characters of each input string"""
def FML(s1,s2):
    length1 = int(len(s1) - 1)
    length2 = int(len(s2) - 1)

    mid1 = int(len(s1) / 2)
    mid2 = int(len(s2) / 2)

    res = s1[0] + s2[0] + s1[mid1] + s2[mid2] + s1[length1] + s2[length2]
    print(res)
FML("Hello", "world")

"""Append new string in the middle of a given string"""
s1 ="Ault"
s2 = "Kelly"

length = int(len(s1))
mids1 = int(len(s1)/2)

res = s1[:mids1]

res = res+s2
print(res)

res = res + s1[mids1:]
print(res)

"""Write a program to create a new string made of the middle three characters of an input string."""
str1 = "JaSonAy"

mid = int(len(str1)/2)
print(mid)

res = str1[mid-1] + str1[mid] +str1[mid+1]
print(res)