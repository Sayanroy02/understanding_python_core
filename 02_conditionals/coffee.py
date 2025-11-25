coffee_size = input("What size coffee do you want? (small, medium, large): ").strip().lower()
extra_shot = input("Do you want an extra shot of espresso? (yes/no): ").strip().lower()


if extra_shot == "yes":
    order = coffee_size + " coffee with an extra shot"
else:
    order = coffee_size + " coffee"


print("You ordered a", order)
