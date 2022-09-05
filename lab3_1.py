class Stack :
    def __init__(self, elements = None) :
        if elements == None or elements == [] :
            self.elements = []
        else :
            self.elements = elements
    def push(self, data) :
        self.elements.append(data)
    def size(self) :
        return len(self.elements)
    def pop(self) :
        return self.elements.pop()
    def display(self, data) :
        if data == 'P' :
            print("Pop = {} and Index = {}".format(self.elements[-1], len(self.elements)-1))
        else :
            print("Add = {} and Size = {}".format(data, len(self.elements)))

n = input("Enter Input : ").split(',')
m = []
s = Stack()

for x in n :
    m.append(x.split())
for x in m :
    if x[0] == 'A' :
        s.push(x[1])
        s.display(x[1])
    elif x == ['P'] :
        if s.elements == [] :
            print(-1)
        else :
            s.display(x[0])
            s.pop()
print("Value in Stack = ", end='')
if s.elements == [] :
    print("Empty")
else :
    for x in s.elements :
        print(x, end=' ')

