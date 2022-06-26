#loops
#for loop
uselessfellows=["mamatha","ashwathi","shilpa","prabakar","tarun" ,"eshwar"]
print(uselessfellows)

#while loop
temp = 77
#68 - 77 F
while temp >=68 and temp <= 77:
    print("Room temp is maintained at {} deg F".format(temp))
    temp = temp-1
    while True:
        print("This loop runs forever")

#nested loop: a loop inside a loop.

number = 1
for row in range(1,4):
    for column in range(1,4):
        print(number, end = ' ')
        number = number + 1
    print()