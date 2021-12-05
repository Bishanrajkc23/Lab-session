# Take username and password from user and check it again for the three times whether the user has entered the right
# username and password. If yes then print a message "Logged in Successfully.
x = str(input("enter username :"))
a = input("enter password in number only :")
for i in range(3):
    if int(a) == 123:
        print("You have login successfully")
        break
else:
        print("Try again")
        a=input("Error,  Please enter pw again")
        for i in range(3):
            if int(a) == 123:
                print("You have login successfully")
                break
        else:
            print("Try again")
            a = input("Error,  Please enter pw again")
            for i in range(3):
                if int(a) == 123:
                    print("You have login successfully")
                    break
            else:
                print("Now you cannot enter BLOCKED!")
