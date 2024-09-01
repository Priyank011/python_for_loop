n=5
row=1
col=1
for row in range(n):
    for col in range(row+1):
        print("*",end="")
    print()