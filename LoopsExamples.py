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
