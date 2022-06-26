#stringname = "string" or 'string'

fruits = "APPLE"
print(fruits)
print(fruits[1])
print(len(fruits))

string = 'string is one among python\'s data type'
print(string)

#string holder or place holder

pgm = "python"
print("{} is a great programming language for beginners".format(pgm))

demo = "python programming is easy"
print(demo.upper())

demo = "python programming is easy"
print(demo.lower())

demo = "python programming is easy"
print(demo.replace("easy","powerful"))

demo = "python programming is powerful"
print(demo.replace("powerful","tough"))


#slice
print(demo[0:5])
print(fruits[0:2])
print(demo[0:14:3])

#LIST
#listname = [obj1, obj2, obj3]
favfruits = ["Apple", "Mango", "Orange"]
print(favfruits)
print(favfruits[1])
print(favfruits[0])
favfruits[1] = "strawberry"
print(favfruits)

#how to add a value at the end
favfruits.append("kiwi")
print(favfruits)

#how to insert values
favfruits.insert(1,"Tomatoes")
print(favfruits)

#removing particular value from list
favfruits.remove("strawberry")
print(favfruits)

#in the alphabetical order
favfruits.sort()
print(favfruits)

favfruits.reverse()
print(favfruits)

#pop will pull the last value and delete it
favfruits.pop()
print(favfruits)


#TUPLE(anything tat doesnt change. for ex: Dob). Tuple cannot assign any values it can only delete the values.
#tuplename = (obj1, obj2)
wardates = (1914,1939)
print(wardates[0])
#wardates[1] = 2022
print(wardates)


#A tuple is a container that holds many objects under a single name.
#A tuple is immutable which means a tuple once defined cannot be modified.


#DICTIONARY
#dictionaryname = {key1:value1, key2:value2, key3:values3}

cameras = {"sony":600, "nikon":600, "canon":700}
print(cameras)

#replacing value
cameras["nikon"] = 700
print(cameras)

#printing keys and values separately
print(cameras.keys())
print(cameras.values())

#deleting a value but only key has to printed to delete
del cameras["sony"]
print(cameras)

#clearing the data and the output must be displayed in flower bracket
cameras.clear()
print(cameras)



