#Palindrome by without converting to string
class Solution:
    def isPalindrome(self, x) -> bool:

        if x<0:
            return False
        rev = 0
        ori = x

        while x>0:
            rev = (rev * 10) + (x % 10)
            x //= 10

        return rev == ori


x = int(input("Enter number:"))
s = Solution()
print(s.isPalindrome(x))


#Palindrome by converting to string

"""class Solution:
    def isPalindrome(self, x) -> bool:
        xstr = str(x)

        rev = xstr[::-1]

        if xstr == rev:
            print(True)
        else:
            print(False)

x= int(input("Enter number:"))
s=Solution()

s.isPalindrome(x)"""




