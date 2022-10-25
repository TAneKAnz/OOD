def dec2bin(n):
    if n == 0:
        return '0'
    else:
        return dec2bin(n//2) + str(n%2)

def o2n(n, i):
    if n > 0 :
        o2n(n-1, i)
        print(str(int(dec2bin(n))).zfill(i))
    elif n == 0 :
        print(str(int(dec2bin(n))).zfill(i))
    else :
        print("Only Positive & Zero Number ! ! !")

i = int(input("Enter Number : "))
if i <= 1 :
    n = i
else :
    n = (2**i)-1
o2n(n, i)