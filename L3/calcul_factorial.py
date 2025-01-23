x = int(input("Enter a number: "))
factorial = 1
for i in range(x,1,-1):
    factorial = factorial * i
print(f"The factorial of the number {x} is {factorial}.")