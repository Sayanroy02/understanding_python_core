print("This is password Strength Checker")

password = input("Enter your password: ")

if len(password) < 6:
    print("Weak password")
elif len(password) <=10:
    print("Moderate password")
else:
    print("Strong password")
