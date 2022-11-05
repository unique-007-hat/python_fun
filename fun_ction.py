name = input("Enter your username: ")
passwd = input("Enter password: ")
def my_pro():
    if passwd == "Welcome@123":
       pass1 = input("Create new password: ")
       pass2 = input("Confirm password: ")
       pass
    else:
        print("Wrong password..!")
        quit()
    if pass1 == pass2:
        print("Password changed successfully")
        print("Please login...!")
        pass
    else:
        quit()
    name2 = input("Enter username: ")
    if name == name2:
        pass
    else:
        print("username doesn't match..!")
        quit()
    pass3 = input("Enter password: ")
    if pass3 == pass2:
        pass
        print("Logged in successfully..!")
    else:
        print("password doesn't match please try again...")
        quit()


my_pro()


