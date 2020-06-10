from OopsDemo import Calculator


class Childmp1(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 2, 10) # You have to call parent constructor if it got any method

    def getCompeleteData(self):
        return self.num2 + self.num + self.Add()


obj = Childmp1()
print(obj.getCompeleteData())

