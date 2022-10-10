class LinkedList :
    class Node :
        def __init__(self, data, next = None) :
            self.data = data
            if next == None :
                self.next = None
            else :
                self.next = next
        
    def __init__(self) :
        self.head = None

    def append(self, data) :
        node = self.Node(data)
        if self.head == None :
            self.head = node
        else :
            t = self.head
            while t.next != None :
                t = t.next
            t.next = node

    def __str__(self) :
        s = ''
        t = self.head
        while t.next != None :
            s += str(t.data) + " <- "
            t = t.next
        s += str(t.data)
        return s

    def arrange(self) :
        t = self.head
        if t.data != '0' :
            while t.next != None :
                t = t.next
                if t.data == '0' :
                    newhead = t
            t.next = self.head
            while t.next.data != '0' :
                t = t.next
            t.next = None
            self.head = newhead
        
lists = LinkedList()
list = input(' *** Locomotive ***\nEnter Input : ').split(" ")
for x in list :
    lists.append(x)
print("Before : " + str(lists))
lists.arrange()
print("After : " + str(lists))