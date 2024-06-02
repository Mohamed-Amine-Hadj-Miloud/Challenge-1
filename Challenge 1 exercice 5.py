password = "exsrdctfvyhni"
if len(password) >= 8 and any(i.isdigit() for i in password):
    print("strong password")
else : print("weak password")
input("press enter to exit")