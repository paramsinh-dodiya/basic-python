class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stoped..")

class Toyotacar(car):
    def __init__(self,name,type):
        super().__init__(type)
        super().start()
        self.name=name
        

car1=Toyotacar("fortuner","disel")

print(car1.type) 