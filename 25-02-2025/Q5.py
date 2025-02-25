username = input()

if username == "admin":
    print("Enter password:")
    password = input()
    if password == 12345:
        print("login successful")
    else:
        print("incorrect username")
else:
    print("Incorrect username")