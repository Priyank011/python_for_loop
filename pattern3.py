n=5
row=1
while(row<=n):
    n=5
    col=1
    while(col<=row):
        print(row, end=" ") # end=" "  only for same line print.
        col=col+1
    print() # for next line  because print have by defoult end 
    #"\n" it means next print start from next line
    row=row+1