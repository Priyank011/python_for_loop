n=5
for row in range(n):
    for col in range(row+1):
        print(" ",end="")
    for col in range(n-row):
        print("*",end="")
    print("")