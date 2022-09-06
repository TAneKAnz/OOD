class Queue :
    def __init__(self, items = None) :
        if items == None or items == [] :
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
r = Queue()
n = input("Enter Input : ").split(',')
m = []
for x in n :
    m.append(x.split())
for x in m :
    if x[0] == 'E' :
        q.enQueue(x[1])
        print(", ".join(q.items))
    elif x[0] == 'D' :
        if q.isEmpty() :
            print("Empty")
        else :
            if q.size() == 1 :
                q.enQueue("Empty")
            t = q.deQueue()
            r.enQueue(t)
            print("{} <- {}".format(t, ", ".join(q.items)))
            if q.items[0] == "Empty" :
                q.deQueue()
if q.isEmpty() :
    q.enQueue("Empty")
if r.isEmpty() :
    r.enQueue("Empty")
print("{} : {}".format(", ".join(r.items), ", ".join(q.items)))