distance = int(input("Enter the distance to travel (in km): "))

if distance < 3:
    transportation = "Walk"
elif distance <=15:
    transportation = "Bike"
else:
    transportantion = "Car"


print("For a distance of", distance , "km you should use" ,transportation)
    
