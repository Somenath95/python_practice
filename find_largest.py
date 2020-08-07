largest = -1
print("Before", largest)

for num in [9, 14, 12, 3, 74, 15]:
    if num > largest:
        largest = num
    print(largest, num)

print("after", largest)