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

n, m = input("Enter Input : ").split("/")
q = Queue(n.split())
m = m.split(',')
p = []
for x in m :
    p.append(x.split())
for x in p :
    if x[0] == 'E' :
        q.enQueue(x[1])
    elif x[0] == 'D' :
        q.deQueue()

while(not q.isEmpty()) :
    if q.deQueue() in q.items :
        print("Duplicate")
        break
    
if q.isEmpty() :
    print("NO Duplicate")