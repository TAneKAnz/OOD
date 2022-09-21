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
    
q = Queue()
a, b = input("Enter Input : ").split('/')
a = a.split(',')
b = b.split(',')
n = []
m = []
for x in a :
    n.append(x.split())
for x in b :
    m.append(x.split())
    
def check(id) :
    for x in n :
        if id == x[1] :
            return x[0]

def search(dept) :
    for x in range(len(q.items)-1, -1, -1) :
        if dept == check(q.items[x]) :
            return int(x + 1)
    return len(q.items)

for x in m :
    if x[0] == 'E' :
        if q.size() >= 2 :
            i = check(x[1])
            j = search(i)
            q.items.insert(j, x[1])  
        else :
            q.enQueue(x[1])
    elif x[0] == 'D' :
        if q.isEmpty() :
            print("Empty")
        else :
            print(q.deQueue())