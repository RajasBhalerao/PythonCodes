# Binary Search Algorithm

def BinarySerach():
    global ilist, target, mid

    for i in range(0, len(ilist)):
        low = 0
        high = len(ilist)
        mid = int((high + low) // 2)

        if ilist[high-1] > ilist[low]:
            if ilist[mid] == target:
                print("The target {} is at the index {} of the list".format(target, mid))
                break
            elif ilist[mid] < target:
                mid = mid + 1
            else:
                mid = mid - 1
        else:
            print("Error: The numbers in the list are not sorted.")
            break


ilist = [int(item) for item in input("Enter a sorted list of numbers using a space: ").split()]
target = int(input("Enter target number:"))
BinarySerach()

