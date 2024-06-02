def code():
    tempcelsius = 22
    i = input("Enter '1' to convert the temperature from Celsius to Fahrenheit.Enter '2' to convert the temperature from Celsius to Kelvin.Enter '3' to exit the program.")
    if i == "1":
        tempfahrenheit = (tempcelsius *(9/5)) + 32
        print(tempfahrenheit)
        input("press enter to exit")
    elif i == "2":
        tempkelvin = tempcelsius + 273.15
        print(tempkelvin)
        input("press enter to exit")
    elif i == "3":
        quit
    else:
        print("you didn't chose one of the options try again")
        code()
code()