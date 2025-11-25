age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age")
elif age < 13:
    print("You are a child as your age is", age)
elif age < 20:
    print("You are a teenager as your age is", age)
elif age<60:
    print("You are an adult as your age is", age)
else:
    print("You are a senior citizen as your age is", age)


