import statistics
print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))
if n >= 1 and n <= 20 :
    vote = []
    for x in input().split() :
        if int(x) >= 0 :
            vote.append(int(x))
        else :
            print("*** No Candidate Wins ***")
            break
    print(statistics.mode(vote))
else :
    print("*** No Candidate Wins ***")