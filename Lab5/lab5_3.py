class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.sizeof = 0

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.data) + " "
        while cur.next != None:
            s += str(cur.next.data) + " "
            cur = cur.next
        return s

    def reverse(self):
        if(self.head != None):
            prevNode = self.head
            tempNode = self.head
            curNode = self.head.next
            
            prevNode.next = None
            prevNode.prev = None
            
            while(curNode != None):
            
                tempNode = curNode.next
                curNode.next = prevNode
                prevNode.prev = curNode
                prevNode = curNode
                curNode = tempNode

            self.head = prevNode 
            
    def append(self, item):
        NewNode = Node(item)
        l = self.head
        if (self.head is None):
            self.head = NewNode
            self.sizeof += 1
            return

        while(l.next):
            l = l.next
        l.next = NewNode
        self.tail = NewNode 
        NewNode.prev = l
        self.sizeof += 1

    def addHead(self, data) :
        p = Node(data, None)
        p.next = self.head
        self.head = p      
        self.size += 1
    
    def mergeLists(self, list,ID):
        if ID == 1:
            self.head.next = list.head
            return
        list.reverse()
        self.tail.next = list.head
        

L1 = LinkedList()
L2 = LinkedList()
inp = list(map(str, input("Enter Input (L1,L2) : ").split(' ')))

inp[0] = list(inp[0].split('->'))
inp[1] = list(inp[1].split('->'))
ID = 0
for i in range(len(inp[0])):
    L1.append(inp[0][i])
    ID += 1
for i in range(len(inp[1])):
    L2.append(inp[1][i])

print("L1    : "+L1.__str__())
print("L2    : "+L2.__str__())
L1.mergeLists(L2,ID)
print("Merge : "+ L1.__str__())