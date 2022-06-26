class calc:

    #class variable
    num = 100
    def getdata(self,a,b):
        self.firstnumber = a
        self.secondnumber = b
        print("Hi i am inside the function")

    def summation(self):
        return self.firstnumber + self.secondnumber + calc.num + self.thirdnumber + self.fourthnumber
    #constructor
    def __init__(self,c,d):
        self.thirdnumber = c
        self.fourthnumber = d
        print("i am running first")


