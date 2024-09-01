x=int(input("Enter First Number"))
y=int(input("Enter First Number"))
z=int(input("Enter First Number"))
if (x>y and x>z):
    print(x,"is a Largest Number")
elif (y>x and y>x):
    print(y,"is a Largest Number")
elif (z>x and z>y):
    print(z,"is a Largest Number")
elif (y>z and x==y):
    print(x,"is a Largest Number")
elif (z>x and z==y):
    print(y,"is a Largest Number")
elif (x>y and x==z):
    print(z,"is a  Largest Number")
else:
    print("All Are Equal")