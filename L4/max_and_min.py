list = []
n = int(input("How many elements does your list have? "))
for i in range(n):
    value = int(input(f"Enter a number to put in the list (list[{i}]): "))
    list.append(value)
min=list[0]
max=list[0]
for i in range(n):
    if list[i]<min:
        min=list[i]
    if list[i]>max:
        max=list[i]
print(f"The min of the list is {min} and the max of the list is {max}.")