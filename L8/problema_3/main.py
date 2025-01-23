from geometry import circle_area, circumference, rectangle_area, perimeter

# Circle
radius = 5
print(f"Aria cercului cu raza {radius} este {circle_area(radius)}")
print(f"Circumferința cercului cu raza {radius} este {circumference(radius)}")

# Rectangle
length = 10
width = 4
print(f"Aria dreptunghiului cu lungimea {length} și lățimea {width} este {rectangle_area(length, width)}")
print(f"Perimetrul dreptunghiului cu lungimea {length} și lățimea {width} este {perimeter(length, width)}")
