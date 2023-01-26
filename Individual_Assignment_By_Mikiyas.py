string = input("Please enter a string: ")

count = {}
for char in string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for char, occurrences in count.items():
    print(f"{char} = {occurrences}")