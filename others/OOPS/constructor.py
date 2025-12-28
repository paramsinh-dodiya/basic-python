class Student:
    # name="parth"
    def __init__(self,fullname):
        self.name=fullname
        print("adding new Student in database")
    

s1=Student("priyank")
print(s1.name)