#Bubble sort

ilist = [int(item) for item in input("Enter a sorted list of numbers using a space: ").split()]
length = len(ilist)
for i in range(length):
    for j in range(0, length-i-1):
        if ilist[j] > ilist[j+1]:
            ilist[j], ilist[j+1] = ilist[j+1], ilist[j]
print("Sorted List is: ", ilist)

