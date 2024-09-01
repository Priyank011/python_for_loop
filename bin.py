n=int(input())
dec=0
pow=0

while n>0:
    l=n%10     #for tha last degit
    exp=l*(2**pow)   # exponantial function
    dec=dec+exp
    n=n//10 #ociean operater
    pow=pow+1
print ("decimal number=",dec)
    