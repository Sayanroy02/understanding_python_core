number = int(input("Enter a number to calculate its factorial: "))
factorial = 1

while number > 1:
    factorial = factorial * number
    number = number - 1
print("Factorial is:", factorial) 