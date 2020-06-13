# Python Array python also pass string in array we can have mulitple vairable
# Array is called list data type
values = [1, 2, "Pranav", 3.4, "Pothiwala"]
print(values[2]), print(values[0]), \
# [-1] We can print last value by passing -1
print(values[-1])
# We can also tell python to print me value between numbers like [1:3]
print(values[1:4])
# In python array is dynamic we can insert the variable in array
values.insert(3, "Jagruti")
print(values[3])
# If you want to add value at end just use append
values.append("End")
print(values)
# We can update value also like i can Pranav PRANAV
values[2] = "PRANAV"
print(values[2])
# You can delete the value also
del values[0]
print(values)
# Now let play with another variable tuple
# Tuple is static once declare we can not change
# Tuple is same as list data type but list is declare in [] tuple is declare in parenthisis ()
# We can not append or update or change value in tuple
val = (1, 2, "Pranav", 3, "Pothiwala", 4)
print(val[0])
print(val[2])
print(val)
# Let try to change value in tuple make Pranav in capital
# val[2] = "PRANAV"
# Lets try to insert value
# Now lets play with another variable which is Dictionary
# Dictionary is declare in curly braces
# Declar multiline comment in Python
"""Python Dictionary is an unordered sequence of data of key-value pair form.
 It is similar to the hash table type. Dictionaries are written within curly braces in the form key:value. 
It is very useful to retrieve data in an optimized way among a large amount of data."""
# To declare string in dictionary we need to use double ""
# value and output we can also reverse data like 1: "A" & "B":2
# We can also put string value = string
a = {1: "a", "b": 2, "xyz": 245, "P": "Hello World"}
print(a["P"])
a = {"username": "Pranav83", "password": "Neelraj08", "P": 8}
print(a["username"]), print(a["password"])
print(a["P"])
# Lets make real time form username and password let declare empty or default dictionary
loginForm = {}
loginForm["username"] = "Pranav83"
loginForm["password"] = "Neelraj08"
loginForm["FirstName"] = "Pranav"
loginForm["LastName"] = "Pothiwala"
loginForm["Gender"] = "Male"
loginForm["Age"] = 37
print(loginForm)
