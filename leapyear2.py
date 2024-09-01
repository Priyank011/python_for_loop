import calendar
year=int(input("Enter The Year "))
if calendar.isleap(year):
    print(f"{year} is a Leap year") # f use foy Year value convert to mutable
else:
    print(year,"is not a Leap year")