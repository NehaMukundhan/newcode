class square:
    def __init__(self,side):
        self.side = side

    def __add__(squareone,square2):
        return((4*squareone.side)+(4*square2.side))

squareone = square(5) #5*4=20
square2 = square(10) #10*4=40
print("sum of the sides of both the square =",squareone+square2)