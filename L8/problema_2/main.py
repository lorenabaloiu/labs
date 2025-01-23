import math_operations as mo

a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))

print(f"Adunare: {a} + {b} = {mo.add(a, b)}")
print(f"Scădere: {a} - {b} = {mo.subtract(a, b)}")
print(f"Înmulțire: {a} * {b} = {mo.multiply(a, b)}")
print(f"Împărțire: {a} / {b} = {mo.divide(a, b)}")