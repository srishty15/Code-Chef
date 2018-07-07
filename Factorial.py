# find the factorial of a number
# t is the number of TestCases
# n is the number of which factoria is found
t = int(input("Enter the Number of Test Cases(1<=t>=100)"))
fact=1
if t >= 1 and t <= 100:
    for i in range(t) :
        n=int(input("Enter the number:"))
        if n >= 1 and n <= 100:
            for i in range(1,n+11):
                fact=fact*i
            print("Factorial is:",fact)
        else:
            print("Value of n exceeds the limit")
else:
    print("Value of Test Cse exceeds the limit")
