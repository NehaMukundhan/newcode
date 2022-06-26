#condtional statements: are a block of statements whose execution depends on a certain condition.
# a simple if condition is one where a block of statement get executed if the condition mentioned in the if ststement evaluates to true.
#if the condition evaluates to false, the block of statement under else is executed.
#elif which stands for else-if.

#if condition
totalmarks = 95

if totalmarks >= 90:
    print("congrats")

#else

totalmarks = 95
if totalmarks >= 900:
    print("congrats")
else:
    print("you have passed")

totalmarks = 60
if totalmarks >= 90:
    print("congrats")
elif totalmarks >=40:
    print("congrats you have cleared the exam")
else:
    print("you have failed")

#nested if condition: an if condition inside an if condiiton is nested if
totalmarks = 100
if totalmarks >= 90:
    print("congrats you have got 'A' grade")
    if totalmarks == 100:
        print("you have secured full marks")


totalmarks = 95
attendance = 93
if totalmarks >=90 and attendance >=90:
    print("you are a very disciplined student")


totalmarks = 95
attendance = 93
if totalmarks >=90 or attendance >=95:
    print("you are a very disciplined student")

fruit = "apple"
if fruit == "mango" or fruit == "apple":
    print("this is my favorite fruit")
