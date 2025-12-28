with open("prac.txt","r") as f:
    data=f.read()

new=data.replace("Java","Python")
print(new)

with open("prac.txt","w") as f:
    f.write(new)