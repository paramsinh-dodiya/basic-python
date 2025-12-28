n=(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x=int(input("search number :"))

i=0
while i<len(n):
    if(n[i]==x):
        print("you searched is on index of:",i)
    i+=1