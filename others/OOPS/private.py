class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass    #private key using in prefix used double underscore (__)

    def reset_pass(self):
        print(self.__acc_pass)

acc1=Account("1234554","skfjd")

print(acc1.acc_no)
print(acc1.reset_pass())