# Problem: Find sum of elements in an array

# Dynamic Input
arr = list(map(int, input("Enter numbers: ").split()))

# Logic
total = 0

for num in arr:
    total += num

# Output
print("Sum of array elements:", total)
