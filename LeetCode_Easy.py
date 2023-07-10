"""VarArgs and DocStrings"""
"""
When we declare a starred parameter such as *param , then all the positional arguments from that point till
the end are collected as a tuple called 'param'.
Similarly, when we declare a double-starred parameter such as **param , then all the keyword arguments from 
that point till the end are collected as a dictionary called 'param'.

"""
def max(x, *y):
    '''Welcome to max function.'''

    for i in y:
        if i > x:
            print("I {} is greater than {}".format(i, x))
        else:
            print("{} is greater than I {}".format(x, i))


"""If you want to print out the comments of a function or code you can use docstrings function to 
do so use. It only runs when the comment is within a function, with ''' ''' and before any loops. """
print(max.__doc__)

max(5, 1, 2, 6, 7)

"""Recursive Palindrome"""

n = int(input("Enter num:"))


def reverse(num):
    if num < 10:
        return num
    else:
        return int(str(num % 10) + str(reverse(num // 10)))


def palin(num):
    if num == reverse(num):
        return 1
    else:
        return 0


if palin(n) == 1:
    print("YEs")
else:
    print("no")
"""Recursive Fibonacci Series"""
"""0,1,1,2,3,5,8,13,21,34...."""

def fibonacci(num):
    first = 0
    second = 1

    if num<0:
        return False
    elif num==1:
        print(first)
    elif num==2:
        print(first)
        print(second)
    else:
        print(first)
        print(second)
        for i in range(0, num-2):
            res = first + second
            first = second
            second = res
            print(res)

num =  int(input("enter num:"))
fibonacci(num)

"""Iterative Fibonacci Series"""
num = int(input("Enter number:"))
first, second = 0, 1
res = 0
for i in range(0, num):
    if i <= 1:
        res = i

    else:
        res = first + second
        first = second
        second = res
    print(res)

"""Prime Numbers"""
n = int(input("Enter number:"))

for i in range(2, n):
    if n % i == 0:
        print("No")
        break
    else:
        print("Yes")
        break

"""Armstrong Numbers"""

num = 371
res = 0
length = len(str(num))

for i in str(num):
    res += int(i) ** length

if res == num:
    print("Yes")
else:
    print("No")

"""20. Valid Parenthese"""
""" We are using a stack linear data structure which uses FILO method. So we are essentially first creating
an empty stack and then just adding the open parentheses and checking if the next char is a closed parentheses
 or not. If yes then we just pop out the pair parentheses and finally if the stack if empty we return True else
 False

 Key ds used:
 1) Stack --> which is FILO
 2) For loop to iterate through the string
 3) If conditions to check if items are present in the dictionary or stack
 """

s = "(])"


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if not stack:
                    return False
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack


sol = Solution()
res = sol.isValid(s)
print(res)

"""14.Longest Common Prefix """

"""In this case we are going to assign the entire first word as the result and then check if the word
is in the list. If not then it will keep on reducing the letters from the end until common prefix is found"""

strs = ["flower", "flow", "flight"]


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = strs[0]
        reslen = len(result)

        for i in strs[1:]:

            while result != i[0:reslen]:
                result = result[0:(reslen - 1)]
                reslen -= 1
                if reslen == 0:
                    return ("")
        return (result)


Sol = Solution()
res = Sol.longestCommonPrefix(strs)
print(res)

"""13. Roman to Integer"""

""" The key point here is that if the letter in string is larger in the dictionary table than the letter which 
follows in the string then the number will be positive and conversely if the letter is smaller and the following
letter is larger then the number will be negative


Largest to Smallest --> Positive
Smallest to Largest --> Negative

"""

s = "MCMXCIV"


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                res -= roman[s[i]]
            else:
                res += roman[s[i]]
        return res


Sol = Solution()
result = Sol.romanToInt(s)
print(result)

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they
add up to target.You may assume that each input would have exactly one solution, and you may not use the same
element twice.You can return the answer in any order."""

num = (2, 4, 6, 1)
target = 3


class solution():
    def twonums(self, num, target):
        dic = dict()
        for i in range(len(num)):
            difference = target - num[i]
            print("num of i:", num[i])
            print("i:", i)
            if difference in dic:
                return [dic[difference], i]
            else:
                dic[num[i]] = i


s = solution()
print(num)

result = s.twonums(num, target)
print(result)
