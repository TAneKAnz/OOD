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
    def insert(self, data):
        if self.root == None:
            self.root=Node(data)
            return self.root
        node = self.root
        while True:
            if data < node.data:
                if node.left == None:
                    node.left =Node(data)
                    return self.root
                node = node.left
            else:
                if node.right == None:
                    node.right = Node(data)
                    return self.root
                node = node.right
    def delete(self, node, data):
        if node is None:    
            print("Error! Not Found DATA")
            return
        if node.data != data:   
            if node.data > data:
                node.left = self.delete(node.left, data) 
            elif node.data < data:
                node.right = self.delete(node.right, data) 
        else: 

            if node.left is None:
                node = node.right
                return node
            elif node.right is None: 
                node = node.left
                return node
            else:
                current = node.right
                while current.left is not None:
                    current = current.left

                node.data = current.data 
                node.right = self.delete(node.right, current.data)
        return node

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = input('Enter Input : ').split(',')
for i in range (len(inp)):
    if inp[i][0] == 'i':
        print("insert " + (inp[i][2:]))
        T.root=T.insert(int(inp[i][2:]))
        T.printTree(T.root)
    if inp[i][0] == 'd':
        print("delete " + (inp[i][2:]))
        T.root=T.delete(T.root,int(inp[i][2:]))
        T.printTree(T.root)