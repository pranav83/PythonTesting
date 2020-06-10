# classes are user defined blueprint or proto type
#class called calculator with methods multiplicatoin add sub division
#class has varialble, instance variables,constructor etc
# constructor name should ___init____
#new keyword is not required

# self keyword is mandatory for calling variable name into method
#instance and class variables have whole different  purpose
#constructor name should be __int__
#new keyword is not required when you create object

class Calculator:
    num = 100 # class variable
    # Default constructor

    def __init__(self, a, b): # this is constructor

        self.firstnumber = a #this is instansiated
        self.secondnumber= b
        print("I am called automatically when object is created  ")

    def getData(self):
        print("I am now executing  as a method in class")

    def Add(self):
        return self.firstnumber + self.secondnumber + Calculator.num


obj = Calculator(2, 3) # sysntax to create object in python
obj.getData()
print(obj.Add())

obj1 = Calculator(4, 5) # sysntax to create object in python
obj1.getData()
print(obj1.Add())


