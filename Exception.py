try:
    length = 10
    width = 0
    length/width
except Exception:
    print("division by zero is not valid plzz change ur input")

try:
    width = 0
    length/width
except ZeroDivisionError:
    print("Division by zero is invalid kindly change the output")
except NameError:
    print("variable has been used before defining it")
finally:
    print("I am running atleast once")

try:
    width = 0
    length / width
except NameError:
    print("Division by zero is invalid kindly change the output")
except ZeroDivisionError:
    print("variable has been used before defining it")
finally:
    print("I am running atleast once")


try:
    width = 0
    length = 10
    length / width
except NameError:
    print("variable has been used before defining it")
except ZeroDivisionError:
    print("Division by zero is invalid kindly change the output")
finally:
    print("I am running atleast once")