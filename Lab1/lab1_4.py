print("*** Fun with Drawing ***")
n = int(input("Enter input : "))
for x in range(2*n-1, 0, -1) :
    for i in range(2*n-1-x) :
        if (i % 2) == 0 :
            print("#",end='')
        else :
            print(".",end='')

    for y in range(2*x-1, (-2)*x+1, -2) :
        if (x % 2) == 1 :
            print("#",end='')
        else :
            print(".",end='')

    for i in range(2*n-1-x, 0, -1) :
        if (i % 2) == 1 :
            print("#",end='')
        else :
            print(".",end='')
    print('')

for x in range(1, 2*n-1, 1) :
    for i in range(2*n-1-x) :
        if (i % 2) == 0 :
            print("#",end='')
        else :
            print(".",end='')

    for y in range(2*x-1, (-2)*x+1, -2) :
        if (x % 2) == 0 :
            print("#",end='')
        else :
            print(".",end='')

    for i in range(2*n-1-x, 0, -1) :
        if (i % 2) == 1 :
            print("#",end='')
        else :
            print(".",end='')
    print('')