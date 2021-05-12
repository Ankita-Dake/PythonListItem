# Access List Item
List1 = [10, 20, 30, 40, 50, 60, 70]
print(List1)

# access the list items by index number.
List1 = [10, 20, 30, 40, 50, 60, 70]
print(List1[2])
print(List1[-1])
print(List1[0:3])
print(List1[:4])
print(List1[5:])

# CHANGE index VALUE
List2 = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
List2[4] = 'Item 6'
print(List2)

# FETCH VALUE WITH LOOP
List1 = [10, 20, 30, 40, 50, 60, 70]
for i in List1:
    print(i)

# CHECK VALUES N LIST WITH LOOP
a = ['Item 1', 'Item2' , 'Item 3', 'Item 4', 'Item 5', 'Item 6']
if 'Item2' in a:
    print("value available")
else:
    print("Value is not available")

# GET LENGTH OF LIST
List1 = [10, 20, 30, 40, 50, 60, 70]
print(len(List1))

# APPEND() METHOD
List1 = [10, 20, 30, 40, 50, 60, 70]
List1.append(100)
print(List1)

# Print ASCII Value of a character
i = 'A'
print('Tne ASCII value of A is' , ord(i) )


# Write a Python program to get the Python version
# you are using.
import sys
print("Python version")
print(sys.version)
print()

print("Version info.")
print(sys.version_info)

# Display the current date and time
import datetime
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%Y %m %d %H : %M : %S"))

# Addition of Element at
# specific Position
# (using Insert Method)
List3 = [1 , 2 , 4 , 5 , 6 , 7 ,8]
List3.insert(3,3 )
List3.insert(0, 0)
print(List3)

List3.remove(3)
print(List3)
List3.remove(0)
print(List3)
List3.pop(1)
print(List3)
