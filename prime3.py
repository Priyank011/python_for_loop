n=1
while (n<=99):
    n=n+1
    if (n==1):
        #print("not a prime number")
        break
    x=2
    while (x<n):
        if(n%x==0): 
            #print( "Is not a Prime Number"
            break
        x=x+1
        if(x==n):
            print(x,"prime")
    