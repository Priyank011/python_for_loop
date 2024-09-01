n=5
row=0
l=(row+1)*2
for row in range(0,n):
    for col in range(row+1):
        print(row*2,end="")
    print()