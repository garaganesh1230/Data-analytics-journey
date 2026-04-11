# Problem: Find largest element in an array

arr = [10, 20, 5, 40, 15]
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)
