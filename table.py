z=int(input("Enter The Number "))
x=1
y=z*10+1
for i in range(x,y+1):
    if i%z==0:
        print(i)