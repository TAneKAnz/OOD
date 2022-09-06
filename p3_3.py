class Stack:
    def __init__(self, items = None) :
        if items == None or items == [] :
            self.items = []
        else :
            self.items = items

    def push(self, i) :
        self.items.append(i)

    def pop(self) :
        return self.items.pop()

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

