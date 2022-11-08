class Node :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None
    def __str__(self) :
        return str(self.data)

class BST :
    def __init__(self) :
        self.root = None
        self.count = 0

    def insert(self, data) :
        node = Node(data)
        if self.root :
            root = self.root
            while True :
                if data < root.data :   
                    if not root.left :
                        root.left = node
                        break
                    root = root.left
                else :
                    if not root.right :
                        root.right = node
                        break
                    root = root.right
        else :
            self.root = node
        return self.root

    def printTree(self, node, k, level = 0) :
        if node != None :
            if node.data <= k :
                self.count += 1
            self.printTree(node.right, k, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, k, level + 1)

T = BST()
inp, k = input("Enter Input : ").split('/')
for x in inp.split(' ') :
    root = T.insert(int(x))
T.printTree(root, int(k))
print('--------------------------------------------------\n' + str(T.count))