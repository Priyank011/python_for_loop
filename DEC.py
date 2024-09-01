# decimal to binary
n= int(input("num:  ")) 
def binary (n):
    if (n>1):
     binary(n//2)
    print(n%2,end='')
n2= binary(n)

    