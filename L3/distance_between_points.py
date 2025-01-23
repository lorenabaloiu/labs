import math
print("Enter the coordinates of the first point:")
Ax = int(input("Ax = "))
Ay = int(input("Ay = "))
print("Enter the coordinates of the second point:")
Bx = int(input("Bx = "))
By = int(input("By = "))
distance = math.sqrt(pow(Ax-Bx,2)+pow(Ay-By,2))
print(f"The distance of the 2 points is {distance:.2f}.")