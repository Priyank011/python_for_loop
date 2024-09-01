def add(x, y): 
    return x + y
def subtract(x, y): 
    return x - y
def multiply(x, y): 
    return x * y
def divide(x, y): 
    return x / y


n1=int (input("first input"))
while True:
    
    choice =  input( " 1=add,2=subtract,3=multiply,4=divide Enter Choice(1/2/3/4)")
    if choice in ('1','2','3','4'):
            n2= int(input("second input"))

    if choice=='1':
            print (n1,"+",n2,"=", add(n1, n2))
            n3=add(n1, n2)
    elif choice =='2':
            print (n1,"-",n2,"=", subtract(n1, n2))
            n3=subtract(n1, n2)
    elif choice =='3':
            print (n1,"*",n2,"=", multiply(n1, n2))
            n3=multiply(n1, n2)
    elif choice =='4':
            print (n1,"/",n2,"=", divide(n1, n2))
            n3=divide(n1, n2)
    else:
            print("Wrong Input") 
    
 
        
    next_calculation = input("let's do next calculation ? (Yes/no):")
    if next_calculation =="no":
        break
    n1=n3
 