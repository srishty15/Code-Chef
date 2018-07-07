# To find the winner of game by the Lead Score
t = int(input("Enter the Number of Test Cases(1<=t>=1000)"))
s1=0
s2=0
if t >= 1 & t <= 1000:
    for i in range(t) :
        print("***ROUND ",i+1,"***")
        n1 = int(input("Enter the score of Player 1"))
        n2 = int(input("Enter the score of Player 2"))
        if n1>n2:
            print("Player 1 leads in Round",i+1)
            s1=s1+(n1-n2)

        elif n2>n1:
            print("Player 2 leads in Round", i + 1)
            s2=s2+(n2-n1)
        else:
            print("Round ",i+1," Draw!")
    if s1>s2:
        print("Player 1 is WINNER by a lead of",s1," scores")
    elif s2>s1:
        print("Player 2 is WINNER by a lead of", s2, " scores")
    else:
        print("Match Draw")
else:
    print("Value of TestCase exceeds the limit")
