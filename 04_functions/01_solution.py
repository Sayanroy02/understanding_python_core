def square_root_of_a_number(number):
    n = number ** 2
    return n


num = int(input("Enter a number to find its square: "))
result = square_root_of_a_number(num)

print("The square of ", num , "is " , result)

