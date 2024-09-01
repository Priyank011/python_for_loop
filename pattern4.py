n=5
for row in range(n):
    for col in range(n-row):
        print("*",end="")
    print()
for row in range(n-1):
    for col in range(row+2):
        print("*",end="")
    print()