n=5
for row in range(n):
    for col in range (n-row-1):
        print(" ",end="")
    for col in range(row+1):
        print("*",end="")
    for col in range(row):
        print("*",end="")
    print()
n=4
for row in range(n):
    for col in range (row+1):
        print(" ",end="")
    for col in range(n-row):
        print("*",end="")
    for col in range(n-row-1):
        print("*",end="")
    print()