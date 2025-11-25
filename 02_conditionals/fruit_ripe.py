fruit = input("Enter the type of fruit (e.g., banana): ")


if fruit == "banana":
    color = input("Enter the color of the fruit: ")
    if  color == "yellow":
        print("The" fruit "is ripe.")
    elif color == "green":
        print("The" fruit "is Unripe.")
    elif color == "brown":
        print("The" fruit "is overripe.")
    else:
        print("Unknown condition of", fruit)
else:
    print("No information about" , fruit , "is available.")