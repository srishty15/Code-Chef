# To find the sum of Digits
t = int(input("Enter the Number of Test Cases(1<=t>=1000)"))
if t >= 1 & t <= 1000:
    for i in range(t) :
        n=int(input("Enter the number:"))
        sum_num = 0
        while n != 0:
            r = n%10
            sum_num = sum_num+r
            n = n//10
        print("Sum of Digits=",sum_num)
else:
    print("Value of TestCase exceeds the limit")


