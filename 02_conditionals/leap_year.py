year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = "is a leap year"
else:
    leap_year = "is not a leap year."
    
print(f"{year} {leap_year}")