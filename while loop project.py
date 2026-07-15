username = "admin"
password = "2908"
balance = 50000

u = input("enter your username : ")
p = input("enter your password : ")

if u == username :
    p = input("enter your confirm password : ")
    if p == password:
        print("Login sucessfull")
    else :
        print("Wrong password")


    print("1. deposit")
    print("2. withdraw")
    print("3. check balance")
    print("4. exit")

    option = int(input("enter your option : "))

    if option == 1:
        amount = int(input("enter your amount to deposit : "))
        balance += amount
        print('your amount deposit sucessfully :', balance)

    elif option == 2 :
        withdraw = int (input ("enter your withdrawal amount : "))
        if withdraw <= balance :
            balance -= withdraw 
            print('your amount withdrawal sucessfully : ', balance)
        else :
            print('insufficient balance :', balance)

    elif option == 3 :
        print('your current balance is : ', balance)



    elif option == 4 :
        print('exit sucessfully ')


    else :
        print('invalid option ')
else :
    print("Invalid Username and Password")    