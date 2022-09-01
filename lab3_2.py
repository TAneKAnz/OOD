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
    def delete(self, data, n) :
        if n == 1 :
            self.items = [x for x in self.items if x != data]
        elif n == 2 :
            self.items = [x for x in self.items if x >= data]
        elif n == 3 :
            self.items = [x for x in self.items if x <= data]
            
n = input("Enter Input : ").split(',')
m = []
s = Stack()
for x in n :
    m.append(x.split())
for x in m :
    if x[0] == 'A' :
        s.push(int(x[1]))
        print("Add = {}".format(x[1]))
        
    elif x[0] == 'P' :
        if s.items == [] :
            print(-1)
        else :
            print("Pop = {}".format(s.items[-1]))
            s.pop()
        
    elif x[0] == 'D' :
        if s.items == []:
            print(-1)
        else :
            for y in s.items :
                if y == int(x[1]) :
                    print("Delete = {}".format(x[1]))
            s.delete(int(x[1]), 1)
        
    elif x[0] == 'LD' :
        if s.items == []:
            print(-1)
        else :
            a = [i for i in s.items]
            a.sort()
            for y in a :
                if y < int(x[1]) :
                    print("Delete = {} Because {} is less than {}".format(y, y, x[1]))
            s.delete(int(x[1]), 2)
        
    elif x[0] == 'MD' :
        if s.items == []:
            print(-1)
        else :
            a = [i for i in s.items]
            a.sort()
            for y in a :
                if y > int(x[1]) :
                    print("Delete = {} Because {} is more than {}".format(y, y, x[1]))
            s.delete(int(x[1]), 3)

print("Value in Stack = {}".format(s.items))