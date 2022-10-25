from re import T


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self) :
        self.head = None
        self.size = 0

    def __str__(self) :
        s = ''
        t = self.head
        while t.next != None :
            s += str(t.data) + '->'
            t = t.next
        s += str(t.data)
        return s

    def isEmpty(self) :
        return self.size == 0

    def append(self, data) :
        node = Node(data)
        if self.isEmpty() :
            self.head = node
        else :
            t = self.head
            while t.next != None :
                t = t.next
            t.next = node
        self.size += 1

    def insert(self, index, data) :
        node = Node(data)
        count = 1
        t = self.head
        while self.size != 0 or t.next != None or count != int(index) :
            count += 1
            t = t.next
        if int(index) == 0 :
            node.next = self.head
            self.head = node
        else :
            node.next = t.next
            t.next = node
        self.size += 1

lists = LinkedList()
inp = input("Enter Input : ").split(',')
if inp[0] == '' :
    print("List is empty")
else :
    for x in inp[0].split(' ') :
        lists.append(x)
    print("link list : " + str(lists))
for x in inp[1:] :
    x = x.split(':')
    if int(x[0]) > lists.size or int(x[0]) < 0:
        print("Data cannot be added")
    else :
        print("index = {} and data = {}".format(int(x[0]), int(x[1])))
        lists.insert(int(x[0]), int(x[1]))
    print("link list : " + str(lists))
