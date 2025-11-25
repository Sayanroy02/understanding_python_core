from datetime import date

age = int(input("Enter your age: "))
todays_date = date.today()
day = todays_date.strftime("%A")  #%A returns use full week name from todays date
ticket_price =  12 if age >=18 else 8 #use condition in one line

if age < 0:
    print("Invalid age")
elif day == "Wednesday":
    ticket_price = ticket_price - 2
    print("It's Wednesday! You get a $2 discount!")
    print("Your Movie ticket price is $", ticket_price)
else:
    ticket_price = ticket_price
    print("Your Movie ticket price is $", ticket_price)
    