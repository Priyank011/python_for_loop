x=int(input("Enter The Year\n"))
if (x%100==0):
    if(x%400==0):
        print(x,"is a Leap Year")
    else:
        print(x,"is not a leap year")
elif(x%4==0):
    print(x,"is a Leap Year")
else:
         print(x,"is not a Leap Year")
        