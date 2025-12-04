def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) #recursive call(recursion)
    
number = int(input("Enter a number to find its factorial: "))
result = factorial(number)
print("The factorial of number ", number , " is " , result)
