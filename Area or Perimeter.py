# To find the Area and Perimeter of Rectangle and print the greatest
l = eval(input("Enter the Length:"))
b = eval(input("Enter the Breadth:"))
if (l >= 1 & l <= 1000) & (b >= 1 & b <= 1000):
    if (l*b) > (2*(l+b)):
        print("Area is Greater \nArea=",l*b)
    elif (l*b) == (2*(l+b)):
        print("Area and Perimeter are Equal")
    else:
        print("Perimeter is Greater \nPerimeter=",(2*(l+b)))


