
"""
Trees:
    -> Non-linear data structures with root and node
    -> The node that precedes is the parent and the node after is called the child.
    -> The last nodes are called the leaves

--------------------
Queue:
    -> based on First In First Out
    -> EnQueue - Addition of elements
    -> DeQueue - Deleting of elements
    -> Similar to stack but only the first element or the 0th element of the list should be pop'ed instead of the
       most recent element added.

--------------------
Stack:
    -> based on principle of Last In First Out
    -> operations:
        -> pushing - add elements
        -> popping - deleting elements
        -> accessing - only from one point in the stack called Top
Importing Stacks:
    -> from collection import deque library - provides stack and queue operations in one object
    -> from queue import LifoQueue library -
---------------------
Sets:
Creation:
    -> {, , ,}
Adding Elements:
    -> add() - Add element to the set
Other functions:
    -> x.union(y) - combines the data present in x and y sets
    -> x.intersection(y) - finds the data present in both the sets
    -> x.difference(y) - deletes any common elements and returns only the uncommon from set x.
    -> x.symmetric_difference(y) - deletes any common elements but returns uncommon elements from both table.

----------------------
Tuple:
Creation:
    -> ()
    -> tuple()
Accessing Elements:
    -> [x:y]
    -> [x][y] - find the y element of the x element in the tuple
Appending Elements:
    -> use the + operator
Other functions:
    -> count() - finds the count of the value passed
    -> index() - finds the index position of the elements in the function.

------------------------
Dictionary:
Creation:
    -> {'x':y, 'p': q}
    -> dict()
Adding/Changing Elements:
    -> Access the key and then change the value accordingly.
    -> To add values, you simply just add another key-value
Deleting Elements:
    -> pop() - returns the value that has been deleted.
    -> popitem() - returns a tuple of the key and value.
    -> clear() - empty the dictionary
Accessing Elements:
    -> can access using keys
    -> get()
Other functions:
    -> keys() - get just the keys
    -> value() - get just the values
    -> items() - get key-value pairs

-------------------------
Lists:
Creation:
    -> []
    -> list()
Adding Elements:
    -> append() - adds all the elements passed to it as a single element
    -> extend() - adds the elements one by one into the list
    -> insert() - adds the element passed to the index value and increase the size of the list
Deleting Elements:
    -> del
    -> pop
    -> remove
    -> clear - empty the list
Accessing Elements
    -> [x:y]
    -> [::-1] -> access elements in reserve
Other functions:
    -> count() -> finds the count of the value passed
    -> len() -> length of thr list
    -> index() -> finds the index value of value passed where it has been encountered the first time.
    -> sort() / sorted() - sort values of the list. sorted () function creates a new sequence type
                           containing a sorted version of the given sequence.

"""