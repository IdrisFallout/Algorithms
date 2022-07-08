from array import *

vals = array('i', [])

x = input("How many numbers do you want to register? ")
i = 0
while i < int(x):
    element = input("Element " + str(i + 1) + ": ")
    vals.append(int(element))
    i += 1

target = input("Enter the number you want to search it's position: ")

for y in sorted(vals):
    if str(y) == target:
        print("Your value(" + target + ") found in position " + str(vals.index(y) + 1))
        break
    elif str(y) > target:
        print("You number in not in your record")
    else:
        print("You number in not in your record")
