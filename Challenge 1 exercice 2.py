def code():
    num1 = 42
    num2 = 58
    i = input("Enter '1' to add num1 and num2. Enter '2' to subtract num2 from num1. Enter '3' to multiply num1 and num2. Enter '4' to divide num1 by num2. Enter '5' to exit the program.")
    if i == "1":
        print(num1+num2)
        input("press enter to exit")

    elif i == "2":
        print(num1-num2)
        input("press enter to exit")

    elif i == "3":
        print(num1*num2)
        input("press enter to exit")

    elif i == "4":
        print(num1/num2)
        input("press enter to exit")

    elif i == "5":
        quit
    else:
        print("you didn't choose one of the options.Try again")
        code()
code()