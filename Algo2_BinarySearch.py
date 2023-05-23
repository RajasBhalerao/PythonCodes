# Binary Search Algorithm
"""As binary serach requires a sorted list, we have also implemented a bubble sort in the code"""

def BinarySerach():
    global ilist, target, mid

    #Bubble sort
    length = len(ilist)
    for i in range(length):
        for j in range(0, length - i - 1):
            if ilist[j] > ilist[j + 1]:
                ilist[j], ilist[j + 1] = ilist[j + 1], ilist[j]
    print("Sorted List is: ", ilist)

    low = 0
    high = len(ilist)-1


    low = 0
    high = len(ilist)-1

    for i in range(0, len(ilist)):
            mid = int((high + low) // 2)
            if ilist[mid] == target:
                print("The target {} is at the index {} of the list".format(target, mid))
                break
            elif ilist[mid] < target:
                low = mid + 1
            else:
                high = mid - 1


ilist = [int(item) for item in input("Enter a sorted list of numbers using a space: ").split()]
target = int(input("Enter target number:"))
BinarySerach()

