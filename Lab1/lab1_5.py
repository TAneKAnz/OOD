n = int(input("Enter Input : "))
for x in range(n+2, 0, -1) :
    for y in range(1, n+3) :
        if y < x :
            print(".", end='')
        if y >= x :
            print("#", end='')
    for y in range(n+2) :
        if y >= 1 and x < n+2 and y < n+1 and x > 1 :
            print("#", end='')
        else :
            print("+", end='')
    print('')

for x in range(n+2, 0, -1) :
    for y in range(n+2) :
        if y >= 1 and x < n+2 and y < n+1 and x > 1 :
            print("+", end='')
        else :
            print("#", end='')
    for y in range(1, n+3) :
        if y <= x :
            print("+", end='')
        if y > x :
            print(".", end='')  
    print('')