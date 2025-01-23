def unique_pair_sum(numbers, target):
    seen = set()
    pairs = set()
    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return pairs

numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
target = int(input("Enter the target value: "))
result = unique_pair_sum(numbers, target)
print("Unique pairs:", result)
