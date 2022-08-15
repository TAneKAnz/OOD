print("*** Fun with Drawing ***")
n = input("Enter input : ")
for x in range(n) :
    print("#")
    for y in range(2*(2*n-1)-1) :
        if (x % 2) == 0 :
            print("#")
        else :
            print(".")
