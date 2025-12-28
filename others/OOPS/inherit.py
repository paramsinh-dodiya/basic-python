#single level inherits

# class car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stoped..")

# class Toyotacar(car):
#     def __init__(self,name):
#         self.name=name

# car1=Toyotacar("fortuner")
# car2=Toyotacar("prius")


# print(car1.start())

#multi level inherits::~~

class A:
    varA="welcome to class A"

class B:
    varB="welcome to class B"

class C(A,B):
    varC="welcome to class C"

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)