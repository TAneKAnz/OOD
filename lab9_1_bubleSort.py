def bubbleSort(l) :
    step = 1
    for i in range(len(l)-2) :
        c = None
        for j in range(len(l)-i-1) :
            if l[j] > l[j+1] :
                c = l[j]
                l[j], l[j+1] = l[j+1], l[j]
        if c != None :
            print(f"{step} step : {l} move[{c}]")
            step += 1
    c = None
    for i in range(len(l)-1) :
        if l[i] > l[i+1] :
                c = l[i]
                l[i], l[i+1] = l[i+1], l[i]
    return f"last step : {l} move[{c}]"

print(bubbleSort(list(map(int, input("Enter Input : ").split()))))

