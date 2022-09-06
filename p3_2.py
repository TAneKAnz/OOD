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

    def peek(self) :
        return self.items[-1]

    def clear(self) :
        self.items = []

def match(x) :
    if s.peek() == '(' and x == ')' :
        return True
    elif s.peek() == '{' and x == '}' :
        return True
    elif s.peek() == '[' and x == ']' :
        return True

def parenthesis() :
    for x in ls :
        if x in '[{(' :
            s.push(x)
        elif x in ']})' :
            if not s.isEmpty() :
                if match(x) :
                    s.pop()
                else :
                    return "Unmatch open-close"
            else :
                return "close paren excess"
    if not s.isEmpty() :
        st = "open paren excess   {} : ".format(s.size())
        while not s.isEmpty() :
            st += s.pop()
        return st
    else :
        return "MATCH"

s = Stack()
str = input("Enter expression : ")
print(str, end=' ')
ls = [x for x in str]
print(parenthesis())