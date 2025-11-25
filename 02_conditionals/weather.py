weather = input("Enter the weather : ").lower()

if weather == "sunny":
    print("It's a sunny day, go for a walk!")
elif weather == "rainy":
    print("It's raining, read a book!")
elif weather == "snowy":
    print("It's snowy, build a snowman!")
else:
    print("Weather not recognized, stay indoors!")


# can do this dynamicall by importing weather from an api
