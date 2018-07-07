# To demonstrate the function of ATM
ch = 'y'
while ch == 'y' or ch == 'Y':
    name = input("Please enter your Name:")
    print("Hello!",name)
    account_id = input("Enter the Account Number:")
    initial_amt = float(input("Enter the amount present in your Account:$"))
    amt_w = float(input("Enter the amount to be Withdrawn:$"))
    if amt_w < initial_amt :
        if amt_w % 5 == 0:
            initial_amt = (initial_amt-amt_w)-0.5
            print("Amount is Withdrawn with a deduction of USD $0.50 \n Transaction Successful!")
        else:
            print("Withdraw amount entered is not a multiple of 5 \n Transaction Failed!")
    else:
        print("Not Sufficient Balance \n Transaction Failed!")
    print("Your current Balance is:$",initial_amt)
    ch=input("Do you want to continue? \n If Yes,Press Y \n If No,Press N")


