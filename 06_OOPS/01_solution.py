class Car(): # Class definition
    total_cars_created=0  # Class variable to keep track of total cars created
    def __init__(self, brand, model):  # Constructor method special
        self.__brand = brand    # now this is private variable and cannot be accesed by object 
        self.__model = model    # Instance variable for model
        # self.total_cars_created += 1  # Increment total cars created (common way)
        Car.total_cars_created += 1  # Increment total cars created (best way)
        
    #q2 method to the Car class that displays the full name of the car (brand and model).
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):            #for polymorphism
        return "Petrol or Diesel"
    
    #q7 static method
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    #property decorator to access private variable brand
    @property
    def model(self):    #now it can be accessed by object but just view only cannot change its value
        return self.__model
    
    

my_car = Car("Toyota", "Corolla") # Creating an instance of Car class
print(my_car.get_brand()) # Accessing and printing the brand of the car
print(my_car.model)
#print for q2
print(my_car.full_name())

#q3 inheritance
class Electric_car(Car): # Electric_car class inheriting from Car class
    def __init__(self , brand , model , battery_size):
        super().__init__(brand , model) # Calling the constructor of the parent class
        self.battery_size = battery_size
    def fuel_type(self):            #for polymorphism
        return "Electric charge" 
    
my_electric_car = Electric_car("Tesla" , "Model x" , "100kWh") # Creating an instance of Electric_car class
print(my_electric_car.full_name() , my_electric_car.battery_size) # Accessing and printing the brand of the electric car

# #encapsulation
my_dream_car = Car("Lamborghini" , "Aventador") #object of Car class
print(my_dream_car.get_brand()) #can access brand by a getter method 



# #polymorphism result by printing fuel type of both car and electric car
print(my_car.fuel_type())
print(my_electric_car.fuel_type())

safari = Car("Ford" , "Safari")
# safari.model = "New Safari"  # trying to change the model of the car will give error as model is property decorator (cannot update the model name once given)
Pagani = Car("Pagani" , "Huayra")
#q6 access the total cars created
print(Car.total_cars_created)

#q7 accessing static method
print(Car.general_description())

#q8 property decorator
print(safari.model)

#q9 isinstance function
print(isinstance(my_electric_car, Car))  # True
print(isinstance(my_electric_car, Electric_car))  # True


#q10 multiple inheritence

class Battery():
    def battery_capacity(self):
        return "Battery capacity is 75kWh"


class Engine():
    def Engine(self):
        return "Engine capacity is 2000cc"

#here this is example of multiple inheritence
class Hybrid_car(Car , Battery , Engine):
    pass # Hybrid_car class inheriting from Car , Battery and Engine class [pass means empty class]

my_hybrid_car = Hybrid_car("Toyota" , "Prius") 
print(my_hybrid_car.battery_capacity()) # Accessing method from Battery class
print(my_hybrid_car.Engine()) # Accessing method from Engine class