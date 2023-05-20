#Linear Search Algorithm

def LinearList ():
    """If you want to assign a value to a name defined outside the function, then you have to tell Python
    that the name is not local, but it is global. We do this using the global statement. It is impossible
     to assign a value to a variable defined outside a function without the global statement."""
    global ilist, target, lenlist
    print("The input list is {} and the target is {}.". format(ilist, target))

    # We can use enumerate() as it produces a dic of index and key inside a list.
    for index, item in enumerate(ilist):
        if item == target:
            print("The target number {} is found at the index {} of the input list.".format(target, index+1))
            break
        elif index == lenlist - 1:
            print("No Match Found in the entire list")
        else:
            continue


ilist = [int(item) for item in input("Enter the list items : ").split()]
lenlist = len(ilist)
target = int(input("Enter Target:"))

LinearList()

"""
Advantages of Linear Search: 
Linear search can be used irrespective of whether the array is sorted or not. It can be used on arrays
of any data type. Does not require any additional memory. It is a well-suited algorithm for small datasets.

Drawbacks of Linear Search:
Linear search has a time complexity of O(N), which in turn makes it slow for large datasets.
Not suitable for large arrays."""