def run_length_encoding(data):
    if not data:
        return ""
    encoded = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            encoded.append(f"{data[i - 1]}{count}")
            count = 1
    encoded.append(f"{data[-1]}{count}")
    return ''.join(encoded)

input_string = input("Enter a string: ")
encoded_string = run_length_encoding(input_string)
print("Original String:", input_string)
print("Encoded String:", encoded_string)
