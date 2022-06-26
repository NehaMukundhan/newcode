
import one

def two():
    print("i am in 2")

print("Top level in 2")

one.func()

if __name__ == 'Two.py':
   print("Two.py is being run directly")
else:
    print("Two.py has been imported")