# To make a calculator of your own
a = eval(input("Enter the number A:"))
b = eval(input("Enter the number B:"))
sign = input("Enter the Operation You want to perform \n + - * / ")
if (a >= -1000 & a <= 1000) & (b >= -1000 & b <= 1000 & b != 0):
        if sign == '+':
            print("Sum of",a,"is",b,":",a+b)
        elif sign == '-':
            print("Difference of", a, "is", b, ":", a - b)
        elif sign == '*':
            print("Product of", a, "is", b, ":", a * b)
        elif sign == '/':
            print("Division of", a, "is", b, ":", a / b)
        else:
            print("Please check your input :)")
else:
        print("Check the Values of A and B")