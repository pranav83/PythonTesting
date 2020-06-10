# Method to open text file
file = open("text.txt")
# how to read content of file
#print(file.read())
print(file.read(5))# read n number of characters

print(file.readline())
print((file.readline()))

file.close()