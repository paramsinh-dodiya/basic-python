#dictionary are use to store data value in key:value pairs
#they are unordered,mutable(changeble)&don't allow duplicate keys

info={

    "name" : "Parth",
    "age" : 19,
    "is_adult" : True,
    "marks": 96.7,
    "subject":["python","c","java"], #list 
}

print(info) 

print(info["subject"]) #separate print value 

info["name"]="Parthsinh" #change the name but here square bracket[] used
print(info) 


#new nul dictinary and add the value 

dic={}

dic["name"]="Parthsinh Gohil"
dic["age"]=18

print(dic)