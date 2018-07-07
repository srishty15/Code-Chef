# To print number of times 4 is present
t = int(input("Enter the Number of Test Cases(1<=t>=1000)"))
if t >= 1 & t <= 1000:
    for i in range(t):
        n = int(input("Enter the Number"))
        count = 0
        while n != 0:
            r = n%10
            if r == 4:
                count = count+1
            n = n//10         # if not floored(//),it will pick up the Float Value
        print("Number of 4 in line",i+1,"=",count)
else:
    print("Test Case Limit Exceeds")
