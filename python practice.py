#creating a variable
demo = 123
print(demo)

demo_123 = "piu"
print(demo_123)
helloworld = 1234


#int and float
salary = 23.9
print(type(salary))
print(int(salary))

new = int(23.9)
print(new)
new1 = float(123)
print(new1)

new2 = 12.8
print(int(new2))

#strings
#indexing
cars = "santro"
print(cars)
print(len(cars))
print(cars[1])
#slice
bikes = "yamaha"
print(bikes[2:6])
print(bikes[0:6])

#string holder
course = "javascript"
print("{} is the toughest language".format(course))
print(course.upper())
print(course.replace("javascript", "java"))

#list
icecreams = ["vanila", "choclate", "mango"]
print(icecreams)
print(icecreams[1])
icecreams[1] = "strawberry"
print(icecreams)
icecreams.append("butterscotch")
print(icecreams)
icecreams.sort()
print(icecreams)
icecreams.reverse()
print(icecreams)
icecreams.insert(2,"blackcurrent")
print(icecreams)
icecreams.remove("blackcurrent")
print(icecreams)
icecreams.pop()
print(icecreams)
icecreams.clear()
print(icecreams)

#dictionary
mobiles = {"samsung":200, "vivo":400, "oppo":600}
print(mobiles)
mobiles["vivo"] = 700
print(mobiles)
print(mobiles.values())
print(mobiles.keys())
del mobiles["samsung"]
print(mobiles)
mobiles.clear()
print(mobiles)

#conditional statements
totalmarks = 100
if totalmarks >= 101:
    print("the statement is wrong")
elif totalmarks >= 90:
    print("ur good")
else:
    print("great")

cars = "benz"
if cars == "audi" and cars == "benz":
    print("this is right")


fruits = "mango"
if fruits =="mango" or fruits == "apple":
    print("hi")

totalmarks = 100
if totalmarks >= 95:
    print("you have cleared")
    if totalmarks == 100:
        print("good")

#break and continue
for number in range (1,10):
    if number == 11:
        break
    else:
        print(number)

for number in range (1,15):
    if number == 20:
        continue
    else:
        print(number)

for fruits in range (1,5):
    if fruits == 6:
        break
    else:
        print(fruits)

for cars in range (1,5):
    if cars == 7:
        continue
    else:
        print(cars)
else:
    print("ur right")

#functions
def neha():
    print("the great")
neha()

length = 10
width = 10
def computearea():
    area = length + width
    print(area)
computearea()

def computearea(length,width):
    area = length * width
    print(area)
computearea(10,10)


