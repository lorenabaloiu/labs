my_list = []
new_list = []
n = int(input("How many elements does your list have? "))
for i in range(n):
    value = int(input(f"Enter a number to put in the list (list[{i}]): "))
    my_list.append(value)
print("The list is:", my_list)
for i in range(n):
    if (i == 0 or my_list[i] != my_list[i - 1]) and (i == n - 1 or my_list[i] != my_list[i + 1]):
        new_list.append(my_list[i])
print("The new list with non-duplicate elements is:", new_list)