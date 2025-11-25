marks = int(input("Enter makrs: "))


if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 90:
    print("Your grade is A")
elif marks >= 80:
    print("Your grade is B")
elif marks >= 70:
    print("Your grade is C")
elif marks >= 60:
    print("Your grade is D")
else :
    print("Your grade is F")
    
