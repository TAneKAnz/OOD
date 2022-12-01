def bubbleSort(l) :
    sorted = False
    while not sorted :
        sorted = True
        for i in range(len(l)-1) :
            if l[i] > l[i+1] :
                sorted = False
                l[i], l[i+1] = l[i+1], l[i]
    return l

list = list(map(int,input("Enter Input : ").split()))
tmp = []
for i in list :
    if i>=0:
        tmp.append(i)
tmp = bubbleSort(tmp)

for i in list :
    if i < 0 :
        print(i,end=' ')
    else :
        print(tmp.pop(0),end=' ')