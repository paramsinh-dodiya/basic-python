class Student:
    college="GECBVN"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        print("adding new Student in database")
    

s1=Student("priyank",99)
print(s1.name,s1.marks)

s2=Student("parthsinh",98)
print(s2.name,s2.marks)

print(s2.college)