import one,Two

def three():
    print("i am in 3")

print("top level in three.py")

one.func()
Two.func()

if __name__ == '__main__':
    print("three.py is being run directly")
else:
    print("three.py has been imported")