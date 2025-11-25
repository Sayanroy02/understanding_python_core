def greet(name = "Guest"):  #If no name is provided, "Guest" will be used as default - approach 1
    message = "Hello " + name + "!"
    return message

name_input = input("Enter your name: ")
print(greet(name_input if name_input!= "" else "Guest")) #If no name is provided, "Guest" will be used as default - approach 2 

 
