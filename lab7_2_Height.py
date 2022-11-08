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
        if self.root :
            root = self.root
            while True :
                if data > root.data :
                    if not root.right :
                        root.right = node
                        height += 1
                        break
                    root = root.right
                else :
                    if not root.left :
                        root.left = node
                        height += 1
                        break
                    root = root.left
                height += 1
        else :
            self.root = node
        if height > self.height :
            self.height = height
        return self.root


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print("Height of this tree is : " + str(T.height))