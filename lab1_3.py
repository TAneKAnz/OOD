import statistics
print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))
if n >= 1 and n <= 20 :
    vote = []
    count = 1
    for x in input().split() :
        if int(x) >= 0 and int(x) <= 20 and count <= n :
            vote.append(int(x))  
            count += 1
        else :
            print("*** No Candidate Wins ***")
            count += 1
            break
        
    if count == n + 1:
        try:
            print(statistics.mode(vote))
        except:
            print("*** No Candidate Wins ***")
        count += 1
else :
    print("*** No Candidate Wins ***")