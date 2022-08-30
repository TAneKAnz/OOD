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
    
n = input("Enter people : ")
m = []
for character in n :
    m.append(character)
q = Queue(m)
c1 = Queue()
c2 = Queue()
count = 0
countC1 = 0
countC2 = 0
while not q.isEmpty() :
    if countC1 == 3 and not c1.isEmpty() :
        c1.deQueue()
        countC1 = 0
    if countC2 == 2 and not c2.isEmpty() :
        c2.deQueue()
        countC2 = 0
        
    if c1.size() < 5 :
        c1.enQueue(q.deQueue())
    else :
        c2.enQueue(q.deQueue())
        
    if c1.size() > 0 :
        countC1 += 1
    if c2.size() > 0 :
        countC2 += 1
    count += 1
    
    print("{} {} {} {}".format(count, q.items, c1.items, c2.items))