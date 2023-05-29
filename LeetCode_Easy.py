"""14.Longest Common Prefix """

"""In this case we are going to assign the entire first word as the result and then check if the word
is in the list. If not then it will keep on reducing the letters from the end until common prefix is found"""

strs = ["flower","flow","flight"]

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = strs[0]
        reslen = len(result)

        for i in strs[1:]:

            while result != i[0:reslen]:
                result = result[0:(reslen-1)]
                reslen -= 1
                if reslen == 0:
                    return("")
        return(result)

Sol= Solution()
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
            if i + 1 < len(s) and roman[s[i]] < roman[s[i+1]]:
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

num = (2,4,6,1)
target = 3

class solution():
    def twonums(self,num, target):
        dic = dict()
        for i in range(len(num)):
            difference = target -num[i]
            print("num of i:",num[i])
            print("i:", i)
            if difference in dic:
                return [dic[difference], i]
            else:
                dic[num[i]] = i


s = solution()
print(num)

result = s.twonums(num,target)
print(result)
