input_str = input("Enter your name: ")
reverse_str = ""
#reverse a string using loop

for char in input_str:
    reverse_str = char + reverse_str
    
print("Reversed string is:", reverse_str)