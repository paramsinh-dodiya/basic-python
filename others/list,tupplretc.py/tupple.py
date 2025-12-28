#tupple:~A BUILT-IN TYPE THAT LETS US CREATE IMMUTABLE SEQUENCE OF VALUES
#LAST ELEMENT INCLUDE ,(COMA) IN TUPPLE 

tup=(1,2,3,4,2)
print(type(tup))

print(tup[1:3])

print(tup.index(3))  #return index of firdt occurrence means element are which at index
  
print(tup.count(2))  #number count in tupple 