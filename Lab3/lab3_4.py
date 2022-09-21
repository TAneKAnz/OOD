class StackCalc :

    value = 0
    invalid = False

    def __init__(self, items = None) :
        if items == None or items == [] :
            self.items = []
        else :
            self.items = items

    def run(self, arg) :
        ls = arg.split()
        for x in ls :
            if x == '+' :
                result = int(self.pop()) + int(self.pop())
                self.push(result)
                self.value = result
            elif x == '-' :
                result = int(self.pop()) - int(self.pop())
                self.push(result)
                self.value = result
            elif x == '*' :
                result = int(self.pop()) * int(self.pop())
                self.push(result)
                self.value = result
            elif x == '/' :
                result = int(self.pop()) / int(self.pop())
                self.push(result)
                self.value = result
            elif x == "DUP" :
                self.dup()
            elif x == "POP" :
                self.pop()
            elif x == "PSH" :
                pass
            elif x < '*' or x > '9' :
                self.invalid = True
                self.push(x)
                break
            else :
                self.push(x)
        if self.value == 0 :
            if self.items != [] :
                self.value = self.items[-1]

    def push(self, i) :
        self.items.append(i)
    
    def pop(self) :
        return self.items.pop()

    def delete(self, i) :
        self.items.remove(i)

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

    def dup(self) :
        return self.push(self.items[-1])

    def getValue(self) :
        return int(self.value) if self.invalid == False else "Invalid instruction: {}".format(self.items[-1])

print("* Stack Calculator *")
arg = input("Enter arguments : ")
machine = StackCalc()
machine.run(arg)
print(machine.getValue())
