class Stack :
    def __init__(self, items = None) :
        if items == None or items == [] :
            self.items = []
        else :
            self.items = items
    def push(self, data) :
        self.items.append(data)
    def pop(self) :
        return self.items.pop()
    def delete(self, data) :
        self.items.remove(data)

s = Stack([1,1,1,1,2,1])
print(s.delete)