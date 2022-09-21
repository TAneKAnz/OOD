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

    def delete(self, data) :
        self.items.remove(data)

print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split()


m,n = int(m),int(n)
if s == '0' :
    s = []
else :
    s = [int(x) for x in s.split(',')]
st = Stack(s)
if o == "arrive" :
    if n in st.items :
        print("car {} already in soi".format(n))
    elif st.size() == m :
        print("car {} cannot arrive : Soi Full".format(n))
    else :
        st.push(n)
        print("car {} arrive! : Add Car {}".format(n ,n))
elif o == "depart" :
    if st.isEmpty() :
        print("car {} cannot depart : Soi Empty".format(n))
    elif n not in st.items :
        print("car {} cannot depart : Dont Have Car {}".format(n, n))
    else :
        st.delete(n)
        print("car {} depart ! : Car {} was remove".format(n, n))

print(st.items)