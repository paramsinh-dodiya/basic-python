#set is the collection of the unordered items.tupple are allow
#Each element in the set must be unique & immutable. list and dictionary not allowed
#not repeated value stored


seet={1,2,3,2,4,5,4,"parth","GOhil","parth"}

print(seet)
print(len(seet))


col={} #empty dictionary syntax not a empty set
print(type(col))


#create empty set

sel=set()
print(type(sel))

print()

sel.add(1)
sel.add(2)
sel.add((1,2,3,4,5))#tupple add 

print(sel)

sel.remove(2)
print(sel)

sel.clear()
print(len(sel))


print()
pas={"parth","gohil",19,"python","web developer","hacker"}
print(pas.pop())
print(pas.pop())
