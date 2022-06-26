from oops import calc
class child(calc):
    num3 = 400
    def getcomputedata(self):
        return self.num3 + self.summation()
    def __init__(self):
        calc.__init__(self,2,10)
obj = child()
obj.getdata(10,10)
print(obj.getcomputedata())