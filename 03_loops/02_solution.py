number = int(input("Enter a number: "))
sum_of_even_numbers = 0

for i in range(1, number + 1):
    if i % 2 == 0:
        sum_of_even_numbers += i
print("Sum of even numbers from 1 to", number, "is:", sum_of_even_numbers)
        
        