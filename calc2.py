def add(x, y): 
    return x + y
def subtract(x, y): 
    return x - y
def multiply(x, y): 
    return x * y
def divide(x, y): 
    return x / y
def square(x): 
    return (x*x)
def cube(x): 
    return (x*x*x)
n1=int (input("first input"))
while True:
    
    choice =  input( " 1=add,2=subtract,3=multiply,4=divide,5=square,6=cube Enter Choice(1/2/3/4/5/6/7/8/9)")
    if choice=='5':
            print (square(n1))
            n3=n2=square(n1) 
    elif choice=='6':
            print (cube(n1))
            n3=n2=cube(n1)       
    elif choice=='1':
            n2= int(input("second input"))
            print (n1,"+",n2,"=", add(n1, n2))
            n3=add(n1, n2)
    elif choice =='2':
            n2= int(input("second input"))
            print (n1,"-",n2,"=", subtract(n1, n2))
            n3=subtract(n1, n2)
    elif choice =='3':
            n2= int(input("second input"))
            print (n1,"*",n2,"=", multiply(n1, n2))
            n3=multiply(n1, n2)
    elif choice =='4':
            n2= int(input("second input"))
            print (n1,"/",n2,"=", divide(n1, n2))
            n3=divide(n1, n2)
    else:
            print("Wrong Input") 
    
 
        
    next_calculation = input("let's do next calculation ? (Yes=1/no=2/clear=3):")
    if next_calculation =="2":
        break
    if next_calculation =="3":
        n1=int (input("first input"))
    if next_calculation =="1":
        n1=n3
    else:
        print("Wrong Input") 
    