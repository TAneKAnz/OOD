class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.height = 0

    def insert(self, data):
        node = Node(data)
        height = 0
        if self.root:
            root = self.root
            while True:
                if data < root.data:
                    if not root.left:
                        root.left = node
                        height += 1
                        break
                    root = root.left
                else:
                    if not root.right:
                        root.right = node
                        height += 1
                        break
                    root = root.right
                height += 1
        else:
            self.root = node
        if height > self.height :
            self.height = height
        return self.root
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def checkpos(self, x, node = None, level = 0) :
        if level == 0 :
            node = self.root
        if node != None:
            if x == node.data :
                if level == 0 :  
                    return print("Root")
                elif level == self.height :
                    return print("Leaf")
                else :
                    return print("Inner")
            self.checkpos(x, node.right, level + 1)
            self.checkpos(x, node.left, level + 1)
        if level == 0 and node == None:
            return print("Not exist")


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in range(1, len(inp)):
    root = T.insert(inp[i])
T.printTree(root)
T.checkpos(inp[0])