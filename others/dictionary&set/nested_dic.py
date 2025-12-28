student={
    "name":"parth",
    "subject" : {
        "phy":97,
        "math":99,
    }
}

print(student)

print(list(student.keys()))   #or values
print(list(student.values())) 
print(student.items())
pairs=list(student.items())
print(pairs[0])

#get method

print()
print(student["name"])  
print(student.get("name"))  #get method 

# print(student["name1"])  #error ->code not run
# print(student.get("name1"))  #no error -> none return


#upadate method

print()

student.update({"city":"kodinar"})
print(student)