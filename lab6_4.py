def pantip(i, arr):
    path = []
    backtracking(arr, path, 0, [] , i)
    return path
    
def backtracking(arr, path, n, cur, i):
    if i == 0:
        if cur != [] :
            path.append(list(cur))
        cur = []
    prev = 0
    if n < len(arr):
        if prev != arr[n]:
            cur.append(arr[n])
            backtracking(arr, path, n + 1, cur, i - arr[n])
            cur.pop()
            prev = arr[n]
        n += 1
        backtracking(arr, path, n, cur, i)

inp = input('Enter Input (Money, Product) : ').split('/')
arr = [int(i) for i in inp[1].split()]
pattern = pantip(int(inp[0]),arr)
for item in pattern :
    for element in item :
        print(element,end = " ")
    print("")
print("Krisada can purchase Product: {0} with: {1} Baht | {2} Pattern".format(arr, inp[0], len(pattern)))