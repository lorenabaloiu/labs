tuple = []
n = int(input("How many elements does your tuple have? "))
for i in range(n):
    value = int(input(f"Enter a number to put in the tuple (tuple[{i}]): "))
    tuple.append(value)
x = int(input("Enter the number you want to search: "))
ok = 0
copy_i = -1
for i in range(n):
    if tuple[i]==x:
        ok = 1
        copy_i = i
if ok == 1:
    print(f"The number you searched for is in the tuple and it's at {copy_i} position.")
else:
    print("The number you are searching for doesn't exist in the tuple!")