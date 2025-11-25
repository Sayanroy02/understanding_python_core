input_str = input("Enter a string: ")

for char in input_str:
    if input_str.count(char) == 1:
        print ("First non-repeating character is:", char)
        break
