# Accessing parts oof a string
# str=[staring_ind:ending_ind] here ending_ind is not included str[1:4] only 1,2,3 are access not 4 th index number


str='parthsinh Gohil'
print(str[1:4])
print(str[ :4]) #[0:4]
print(str[0: ]) #[0:length of string] or[0:len(str)]

#negative index counting is last character to first character means 
# P  a  r  t  h
#-5 -4 -3 -2 -1    ending_ind(-1) not include
print()
str1="Parth"
print(str1[-5 :-1])