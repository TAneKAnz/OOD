print("*** Converting hh.mm.ss to seconds ***")
a, b, c = [int(x) for x in input("Enter hh mm ss : ").split()]
if (a < 0) :
    print(f'hh({a}) is invalid!')
elif (b < 0 or b >= 60) :
    print(f'mm({b}) is invalid!')
elif (c < 0 or c >= 60) :
    print(f'ss({c}) is invalid!')
else :
    d = 3600*a + 60*b + c
    print("{:02d}:{:02d}:{:02d} = {:,} seconds".format(a, b, c, d))