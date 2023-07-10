"""Monk and Rotation
Monk loves to preform different operations on arrays, and so being the principal of Hackerearth School,
he assigned a task to his new student Mishki. Mishki will be provided with an integer array A of size N
and an integer K , where she needs to rotate the array in the right direction by K steps and then print
the resultant array. As she is new to the school, please help her to complete the task.


Input:
The first line will consists of one integer T denoting the number of test cases.
For each test case:
1) The first line consists of two integers N and K, N being the number of elements in the array and K
denotes the number of steps of rotation.
2) The next line consists of N space separated integers , denoting the elements of the array A.

Output:
Print the required array.


Sample Input
1
5 2
1 2 3 4 5
Sample Output
4 5 1 2 3
"""

"""def Leftrotate():
    if len(str) > interval:
        newstr = str[interval:] + str[0:interval]
        print(newstr)
    else:
        no_rotate = interval - len(str)
        newstr = str[no_rotate:] + str[0:no_rotate]
        print(newstr)
def rightrotate():
    no_rotate = len(str) - interval
    newstr = str[no_rotate:]  # difference to the last element
    newstr += str[0:no_rotate]  # newstr + remaining elements
    print(newstr)


str = input("Enter string:")
interval = int(input("Enter interval:"))
rotation = input("Enter rotation type:")


if rotation == "Left" or rotation == "left":
    Leftrotate()
elif rotation == "Right" or rotation == "right":
    rightrotate()
elif rotation == "Both" or rotation == "both":
    Leftrotate()
    rightrotate()
else:
    print("Error. Invalid input for rotation.")"""

T = int(input()) #Test cases
while T > 0:
    N, K = (input().split()) #number of elements in array #number if rotation
    A = [int(i) for i in input().split()]
    C = []
    if len(A)==int(N):
        for i in range(len(A)):
            B = []
            for j in range(1,int(K)+1):
                B.append(A[-j])
            C = B[::-1]
            remaining = int(N) - int(K)
            C.extend(A[0:remaining])
        for k in C:
            print(k,end=" ")

        T -= 1
    else:
        break