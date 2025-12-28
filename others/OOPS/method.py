class Student:
    # name="parth"
    def __init__(self,fullname):
        self.name=fullname
        print("adding new Student in database")

    def hello(self):
        print("hello",self.name)

s1=Student("priyank")
print(s1.name)

s1.hello()