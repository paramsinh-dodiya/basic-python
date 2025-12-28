def show(n):
    if(n==0):      #condition is important
        return
    print(n)
    show(n-1)

show(5) #5,4,3,2,1 print use recursion