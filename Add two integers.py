# find the sum of two integers
# t is number of test cases
# a and b are the integer values
t = int(input("Enter the Number of Test Cases(1<=t>=1000)"))
if t >= 1 & t <= 1000:
    for i in range(t) :
        a= int(input("Enter the Value of A (1<=a>=10000)"))
        b = int(input("Enter the Value of B (1<=b>=10000)"))
        if a >=1 & a <= 10000:
            if b >=1 & b <= 10000:
                print("Sum is=",a+b)
            else:
                print("Value of B exceeds the limit")
        else:
            print("Value of A exceeds the limit")
else:
    print("Value of TestCase exceeds the limit")
