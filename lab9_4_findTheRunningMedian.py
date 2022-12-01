def bubbleSort(l) :
    if len(l) <= 1 :
        return l
    if len(l) == 2 :
        return l if l[0] < l[1] else [l[1],l[0]]
    a, b = l[0], l[1]
    bs = l[2:]
    r = []
    if a < b :
        r = [a] + bubbleSort([b] + bs)
    else :
        r = [b] + bubbleSort([a] + bs)
    return bubbleSort(r[:-1]) + r[-1:]

def median(l: list) -> float :
    l = bubbleSort(l)
    ind = int(len(l)/2)
    if len(l)%2 != 0 :
        return l[ind]
    return (l[ind]+l[ind-1])/2


l = [e for e in input("Enter Input : ").split()]
if l[0] == 'EX':
    Ans = "xxx"
    print("Extra Question : What is a suitable sort algorithm?")
    print("   Your Answer : "+Ans)
else:
    l=list(map(int, l))
    for i in range(1, len(l)+1) :
        print(f"list = {l[:i]} : median = {median(l[:i]):.1f}")