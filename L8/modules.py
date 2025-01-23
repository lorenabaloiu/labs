import math

num = int(input("Enter a number: "))
angle = int(input("Enter a number of an angle: "))

sqrt_result = math.sqrt(num)

factorial_result = math.factorial(num)

sine_result = math.sin(math.radians(angle))

print(f"Rădăcina pătrată a {num} este {sqrt_result}")
print(f"Factorialul lui {num} este {factorial_result}")
print(f"Sinusul unghiului de {angle} grade este {sine_result}")
