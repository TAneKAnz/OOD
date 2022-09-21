def dec2bin(n):
    if n == 0:
        return '0'
    else:
        return dec2bin(n//2) + str(n%2)

def o2n(n, i, t):
    if n > t and n != 1 :
        if n == 0 :
            print("Only Positive & Zero Number ! ! !")
    elif t == 0 :
        print(0)
    else :
        print(str(int(dec2bin(n))).zfill(i))
        o2n(n+1, i, t)

i = int(input("Enter Number : "))
if i <= 1 :
    t = i
else :
    t = i*i-1
o2n(0, i, t)