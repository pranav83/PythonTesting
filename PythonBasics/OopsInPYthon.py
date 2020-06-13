# Classes are user defined blue print of Method , class variable , instance variable , constructor etc.
class Calculator:
    num = 100
    def getData(self):
        print("This Method In Class")

# Now lets create obj of class in python there is no new operator


obj = Calculator()
obj.getData()
print(obj.num)