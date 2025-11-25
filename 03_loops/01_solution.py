numbers = list(map(int, input("Enter numbers separated by space: ").split())) # Read a list of numbers from user input
positive_number_count = 0
for i in numbers:
    if i > 0:
        positive_number_count += 1
print("Number of positive numbers:", positive_number_count)