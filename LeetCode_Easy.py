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
