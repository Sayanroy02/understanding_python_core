pet = input("What kind of pet do you have? ").strip().lower()

if pet == "dog":
    age = int(input("How old is your dog? "))
    if age < 2:
        food = "puppy food"
    else:
        food = "adult dog food"
elif pet == "cat":
    age = int(input("How old is your cat? "))
    if age > 5:
        food = "senior cat food"
    else:
        fodd ="junior cat food"
else:
    print("Sorry, we don't have food recommendations for that type of pet.")


print(f"For your {pet}, we recommend {food}.")
                  
