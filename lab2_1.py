def Rshift(num,shift):
    bit = []
    tcom = 0
    sum = 0
    
    if num < 0 :
        tcom = 1
        num *= -1
    if (num < shift and tcom == 0) or shift < 0:
        return 0    

    ### Tran 10 to 2 ###
    while num >= 1 :
        t = num % 2
        bit.insert(0, t)
        num //= int(2)

    ### shift bit ###
    if len(bit) <= shift :
        return -1
    else :
        for x in range(shift) :
            bit[-1] = 'k'
            bit.remove('k')

    ### two complement 
    """
    if tcom == 1 :
        for x in range(len(bit)-1) :
            if bit[x] == 1 :
                bit[x] = 0
            else :
                bit[x] = 1
    
    """
    ### Tran 2 to 10 ###
    for x in range(len(bit)) :
        for y in range(x) :
            bit[-1-x] *= 2
        sum += bit[-1-x]
    return sum if (tcom == 0) else sum*(-1)

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))