def sum(n):
    if(n==0):
        return 0
    return sum(n-1)+n

s=sum(n=int(input("enter a num :")))

print(s)