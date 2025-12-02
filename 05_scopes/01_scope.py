#scopes - there are 3 types of scopes
# 1. local scope
# 2. global scope
# 3. built-in scope
#local scope are variables defined inside a function and can only be accessed inside that function
# global scope are variables defined outside a function and can be accessed inside and outside the function
# built-in scope are variables defined by python itself and can be accessed anywhere in the program
# clousures
# nested functions are functions defined inside another function hence called nested functions or clousures

#example of local scope

def func1():
    x = 10  #local scope
    print("Value of x inside func1 is ", x)
    
func1()


# example of global scope

x = 20 #variable declared in global scope and can be accesed anywhere in the program

def func2():
    print("Value of x inside func2 is ", x)
    
func2()


# example of nested functions or clousures 
def func3():
    y = 30  #local scope of func3
    def sub_func():
        print("Value of y inside sub_func is ", y) #accessing variable y from outer function func3
    sub_func()

func3()



#example of built-in scope
print("Value of pi is ", pi)
