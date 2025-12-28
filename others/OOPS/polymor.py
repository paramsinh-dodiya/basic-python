class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownum(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.img
        return Complex(newreal,newimg)
    
    def __sub__(self,num2):
        newreal=self.real-num2.real
        newimg=self.img-num2.img
        return Complex(newreal,newimg)
    
num1=Complex(1,3)
num1.shownum()

num2=Complex(4,6)
num2.shownum()

num3=num1+num2
num3.shownum()

num4=num1-num2
num4.shownum()
# num3=num1.add(num2)
# num3.shownum()