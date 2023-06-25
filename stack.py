class stack:
    def __init__(self):
        self.list = []

    def isnull(self):
        return self.list == []
    def push(self, data):
        return self.list.append(data)
    def pop(self):
        return self.list.pop() #just add self.list.pop(0) to make this a queue algo.
    def disp(self):
        return self.list

S = stack()

while True:
    print("\nselect option: 1) Push (1) +Insert value \
           2) Pop (2) \
           3) Quit (3) ")

    operation = input("Enter option:")
    option = operation.split()

    if option[0] == 'push':
        print("\nPush initialized")
        S.push(int(option[1]))
        print("Updated list is {} ".format(S.disp()))
        print("Push completed")
    elif option[0] == 'pop':
        if S.isnull():
            print("Empty list")
            print("Updated list is {} ".format(S.disp()))
        else:
            print("popped",S.pop())
            print("Updated list is {} ".format(S.disp()))
    else:
        print("Thank you")
        break
