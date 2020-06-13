# While loop is used to check condition it will keep on excuting every time untill condition becomes false
it = 4
#This is infinity loop
while it > 1:
    print(it)
    it = it - 1

while it > 1:
    print(it)
    it = it - 1
# Lets introduce if condition inside while loop
while it > 1:
    if it != 3:
        print(it)
    it = it - 1
# Lets introduce break
while it > 1:
    if it == 3:
        break
    print(it)
    it = it - 1
# Lets use continue
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1