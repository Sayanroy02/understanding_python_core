n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i == 5:
        continue  # Skip the iteration when i is 5
    print(n, "*", i , "=", n * i)