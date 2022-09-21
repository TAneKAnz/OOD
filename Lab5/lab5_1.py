class Node:
    def __init__(self, data, next = None) :
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next

class LinkedList:
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail =  None
            self.size = 0
        else :
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None :
                t = t.next
                self.size += 1
                self.tail = t

    def append(self, data):
        p = Node(data)
        if self.head == None:
            self.head = p
        else :
            t = self.head 
            while t.next != None:
                t = t.next
            t.next = p 
        self.size += 1

    def insert(self, index, data) :
        p = Node(data)
        if index == 0 :
            p.next = self.head
            self.head = p
        else :
            q = self.head
            for j in range(index-1):
                q = q.next
            p.next = q.next
            q.next = p
        self.size += 1

    def isEmpty(self):
        return self.size == 0

    def __str__(self):
        s = ''
        p = self.head
        while p is not None:
            s += str(p.data)+' '
            p = p.next
        return s.split()

L = LinkedList()
inp = input('Enter Input : ').split(',')
if inp[0] == '' :
    print("List is empty")
else :
    print("link list : " + '->'.join(inp[0].split()))
for item in inp[0].split() :
    L.append(item)
for x in inp:
    if ':' in x :
        y = x.split(':')        
        if int(y[0]) >= 0 and int(y[0]) < L.size+1 :
            print("index = {} and data = {}".format(''.join(y[0].split()), y[1]))
            L.insert(int(y[0]), y[1])
            print("link list : "+"->".join(L.__str__()))
        else :
            print("Data cannot be added")
            if inp[0] == '' :
                print("List is empty")
            else :
                print("link list : "+"->".join(L.__str__()))