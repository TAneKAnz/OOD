class Stack():

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

def postFixeval(st):

    s = Stack()

    for x in st :
            if x == '+' :
                result = float(s.pop()) + float(s.pop())
                s.push(result)
                s.value = result
            elif x == '-' :
                result = 0 - (float(s.pop()) - float(s.pop()))
                s.push(result)
                s.value = result
            elif x == '*' :
                result = float(s.pop()) * float(s.pop())
                s.push(result)
                s.value = result
            elif x == '/' :
                a = float(s.pop())
                b = float(s.pop())
                result = b / a
                s.push(result)
                s.value = result
            else :
                s.push(x)

    return s.pop()

print(" ***Postfix expression calcuation***")
token = list(input("Enter Postfix expression : ").split())
print("Answer : ",'{:.2f}'.format(postFixeval(token)))