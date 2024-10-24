# Question 1(i)
# Write a Python program to find the distance between two coordinate points (x1, y1) and (x2, y2).

# import math
# x1 = float(input("Enter x1: "))
# y1 = float(input("Enter y1: "))
# x2 = float(input("Enter x2: "))
# y2 = float(input("Enter y2: "))

# distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# print(f"The distance between coordinate points ({x1}, {y1}) and ({x2}, {y2}) is {distance:.2f} ")







# Question 1(ii)
# Write a Python program to find maximum between three numbers.

number_1 = 34
number_2 = 23
number_3 = 12

if number_1 > number_2 and number_1 > number_3:
    print(f"{number_1} is the maximum")
elif number_2 > number_1 and number_2 > number_3:
    print(f"{number_2} is the maximum")
else:
    print(f"{number_3} is the maximum")