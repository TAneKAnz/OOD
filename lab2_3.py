print("*** New Range ***")

def range(a) :
    m = []
    if len(a) == 1 :
        x = 0
        while x < a[0] :
            m.append(float(x))
            x += 1
    elif len(a) == 2 :
        x = a[0]
        while x < a[1] :
            m.append(float(x))
            x += 1
    elif len(a) == 3 :
        x = a[0]
        while x < a[1] :
            m.append(float("{:.3f}".format(x)))
            x += a[2]

    return m

n = [float(x) for x in input("Enter Input : ").split()]
result = tuple(range(n))
print(result)
