# Problem: Find second largest element in array

arr = [10, 20, 5, 40, 15]

largest = float('-inf')
second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif second < num < largest:
        second = num

print("Second largest element:", second)
