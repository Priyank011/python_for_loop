x=int(input("Range Starting number "))
y=int(input("Range End number "))
z=int(input("Deviser "))
for i in range(x,y+1):
    if i%z==0:
        print(i)