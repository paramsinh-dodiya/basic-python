f = open("demo.txt", "r")
data = f.read(5)
print(data)
print(type(data)) #tempa..
f.close()  # Close the file


#basic mod/char and its meanings:
# 'r'     open for reading(default)
# 'w'     open for writing,truncating the filr first
# 'x'     create a new file and open it for writing
# 'a'     open for writing,appending to the file if it exists
# 'b'     binary mode 
# 't'     text mode(dafault)
# '+'     open a disk file for updating(reading and writing) 

f = open("demo.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)
f.close()