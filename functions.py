#Functions: in this we have to call the function orelse nothing will be executed.
def helloworld():
    print("Hello world")
helloworld()


def helloworld():
    print("Hello World")
def server():
    print("glassfish")
def demo():
    print("i am demo")

helloworld()
server()
demo()


length = 35
width = 45
def computearea():
    area = length * width
    print(area)
computearea()

# another way of executing
def computearea(length, width):
    area = length * width
    print(area)
computearea(25,45)

#Lambda function
x = lambda a : a+35
print(x(35))

x = lambda a,b : a+b
print(x(20,40))

x = lambda a,b,c : a*b*c
print(x(10,10,10))

#another way of executing using both normal and lambda function

def demo():
    x = lambda a : a+10
    print(x(2))
demo()


def func(n):
    return lambda a : a+n
mytripler = func(3)
mydoubler = func(2)

print(mytripler(11))
print(mydoubler(10))

#Function is a named block of reusablr code that performs a specific task.


