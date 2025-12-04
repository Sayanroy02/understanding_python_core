def square_root_of_a_number(number):
    n = number ** 2
    return n  #return the square of the number so that we can pass a number to get square outside the scope of function


num = int(input("Enter a number to find its square: "))  #take user input
result = square_root_of_a_number(num)

print("The square of ", num , "is " , result)

