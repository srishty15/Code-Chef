# To find the divisibility of the numbers input
# T is number of test cases
# K is the number with which divisibility is checked
t = int(input("Enter the Number of Test Cases"))
k = int(input("Enter the Number with which divisibility is to be checked"))
n=[]
for i in range(t):
    x=int(input("Enter the number:"))
    n.append(x)
for i in range(len(n)):
    if n[i]%k==0:
        print(n[i],"is divisible by",k)
    else:
        print(n[i],"is not divisible by",k)



