n=0
while (n<=100):
    print(n)
    n=n+1
    if (n==0):
       print("not a prime number")
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