# Python Array python also pass string in array
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