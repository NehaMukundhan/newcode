import one

def two():
    print("i am in 2")

print("top level in two.py")

one.func()

if __name__ == '__main__':
    print("two.py is being run directly")
else:
    print("two.py had been imported")