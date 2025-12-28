# <var>=(false_value,true_value)[<condition>]

age=int(input("enter your age :"))

vote=("yes","no")[age<18]

print(vote)


print()

sal=float(input("salary :"))
tax=sal*(0.1,0.2)[sal<=50000]
print(tax)


