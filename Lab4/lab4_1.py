class Queue :
    def __init__(self, items = None) :
        if items == None :
            self.items = []
        else :
            self.items = items
        
    def enQueue(self, data) :
        self.items.append(data)
        
    def deQueue(self) :
        return self.items.pop(0)
        
    def isEmpty(self) :
        return len(self.items) == 0
    
    def size(self) :
        return len(self.items)
    
    def pop(self, index) :
        return self.items.pop(index)

q = Queue()
n = input("Enter Input : ").split(',')
m = []
for x in n :
    m.append(x.split())
for x in m :
    if x[0] == 'E' :
        q.enQueue(x[1])
        print(q.size())
    elif x[0] == 'D' :
        if q.isEmpty() :
            print(-1)
        else :
            print("{} {}".format(q.deQueue(), 0))
    
if q.isEmpty() :
    print("Empty")
else :
    while not q.isEmpty() :
        print(q.pop(0), end=' ')