def sort(ls, f, t) :
    if f > t : # None list
        return None
    elif f == t :
        return ls # simple case
    else :
        if ls[f] < ls[f+1] :
            temp = ls[f]
            ls[f] = ls[f+1]
            ls[f+1] = temp
            if f != 0 :
                sort(ls, f-1, t)
        return sort(ls, f+1, t)

ls = [int(x) for x in input("Enter your List : ").split(',')]
print("List after Sorted : {}".format(sort(ls, 0, len(ls)-1)))