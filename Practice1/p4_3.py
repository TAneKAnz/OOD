class Queue: 
    def __init__(self, list = None): 
        if list == None: 
            self.items = []
        else:
            self.items = list

    def enQueue(self, i): 
        self.items.append(i)

    def deQueue(self): 
        return self.items.pop(0)

    def isEmpty(self): 
        return self.items == []

    def size(self): 
        return len(self.items)
        
lst = input("Enter code,hint : ").split(',')
q = Queue()
q.enQueue(list(lst[0]))
q.enQueue(list(lst[1]))
