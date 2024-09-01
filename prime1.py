n=0
if (n==1):
    print("not a prime number")
x=2
while (x<n):
    if(n%x==0):
            print( "Is not a Prime Number")
            break
    x=x+1
    if(x==n):
        print("prime")
x=-2
while (x>n):
    if(n%x==0):
            print( "Is not a Prime Number")
            break
    x=x-1
if(x==n):
    print("prime")
    
            