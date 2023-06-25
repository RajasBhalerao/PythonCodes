class Tree:
    def __init__(self,val):
        self.node = val
        self.left = None
        self.right = None

def printPreorder(root):
    if root:
        print(root.node, end=" ")
        printPreorder(root.left)
        printPreorder(root.right)

if __name__ == "__main__":
    root = Tree(1)
    root.left = Tree(2)
    root.right = Tree(3)
    root.left.left = Tree(4)
    root.left.right = Tree(5)
    root.right.right = Tree(6)

    print("Preorder traversal")
    printPreorder(root)