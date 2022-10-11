class node:
    def __init__(self,data,next = None ):
        self.data = data
        if next == None :
            self.next = None
        else :
            self.next = next
    def __str__(self):
        return self.data

def createList(l=[]):
    head = node(l[0])
    t = head
    for x in l[1:] :
        t.next = node(x)
        t = t.next
    return head

def printList(H):
    while H != None :
        print(H, end=' ')
        H = H.next
    print()

def mergeOrderesList(p,q):
    if int(p.data) < int(q.data) :
        t = p
        s = q
    else :
        t = q
        s = p
    head = t
    while t.next != None and s != None:
        if int(s.data) < int(t.next.data) :
            n = t.next
            t.next = s
            s = s.next
            t.next.next = n
        t = t.next
    if s != None :
        t.next = s
    return head
    
#################### FIX comand ####################   
# input only a number save in L1,L2
L1, L2 = [x.split(',') for x in input("Enter 2 Lists : ").split(' ')]
#L1 = ['1', '3', '5', '7', '10', '20', '22']
#L2 = ['4', '6', '7', '8', '15']
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)