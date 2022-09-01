def match(ar) :
    if len(ar) < 3 :
        return "Array Input Length Must More Than 2"
    else :
        m = []
        for x in range(len(ar)) :
            for y in range(x+1, len(ar)) :
                for z in range(y+1, len(ar)) :
                    if int(ar[x]) + int(ar[y]) + int(ar[z]) == 0 :
                        if not [int(ar[x]), int(ar[y]), int(ar[z])] in m :
                            m.append([int(ar[x]), int(ar[y]), int(ar[z])])
        return m

n = input("Enter Your List : ").split()

print(match(n))