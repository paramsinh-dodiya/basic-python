m=int(input("enter mark :"))

if(m>=90):
    print("garde : A")
elif(90>m>=80):   #elif(m<90 and m>=80)
    print("garde : B")
elif(80>m>=70):
    print("garde : c")
elif(70>m):
    print("garde : D")
else:
    print("Invalid marks")

