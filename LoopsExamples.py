"""Exercise 1: Print First 10 natural numbers using while loop"""
print("Welcome to Exercise 1")
num = 1
while num<=10:
    print(num)
    num = num+1

"""Exercise 2: Print the following pattern"""
print("Welcome to Exercise 2")
tnum = input("Enter number of rows: ")
num = int(tnum)
# The range function has: range (start, end, step); Start is the number by which the iteration begin by default it is 0
# End is the integer at which the iteration ends and Step is the increment by which it will move ahead, default is 1.
for x in range(1, num+1, 1):
    for y in range(1, x+1):
        # here "end" is used to add any string at the end of the output and by default newline charater is added.
        print(y, end=' ')
    print("")

"""Exercise 3: Calculate the sum of all numbers from 1 to a given number"""
fnum = input("Enter number of integers to be added: ")
num = int(fnum)
add = 0
#Method 1: using for loop and range () and creating variable to store the additions.
for i in range(1, num+1, 1):
    add = add + i
print("Sum of integers is:",add)

# Method 2: Using sum() and range()
print("Sum of integers using sum() is:", sum(range(1, num+1)))

"""Exercise 4: Write a program to print multiplication table of a given number"""
fnum = input("Enter the number you want the table for:")
flimit = input("Enter the number where you want to stop the table:")
num = int(fnum)
limit = int(flimit)
multi = 0

for i in range(1, limit+1, 1):
    multi = num * i
    print(multi)

"""Exercise 5: Display numbers from a list using loop"""

numbers = [12,75,150,180,145,525,50]

for i in numbers:
    if i>150:
        continue
    elif i>500:
        break
    elif i % 5 == 0:
        print(i)
"""Create a pathern design"""
for i in range(0,5):
    for j in range(0, i+1):
        print("X", end=' ')
    print("\r")
for i in range(5,0,-1):
    for j in range(0, i-1):
        print("X", end=' ')
    print("\r")


"""Cubing number to a given range"""

num = input("Add number:")
input_number = int(num)

res = 0
for i in range(1,input_number+1):
    res = i * i * i
    print(res)

"""Reversing numbers"""

nums = [1,2,3,4]
nums.reverse()
print(nums)
var1, var2, *remaining = nums
print(var1,var2, *remaining)

num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print("Revere Number ", reverse_number)



"""Factorial of a given number"""
inum = input("Enter number:")
num = int(inum)
count = 1
res = 1
for i in range(num, 0, -1):
    res = int(res * count)
    count = i
print(res)



"""Fibonacci Sequence"""

start = 0
end = 10


num1 = 0
num2 = 1
for i in range(start,end):
    print(num1)
    result = num1 + num2

    num1 = num2
    num2 = result

"""Prime numbers in a range"""
start = 25
end = 50

for num in range(start,end):
    if num >1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)