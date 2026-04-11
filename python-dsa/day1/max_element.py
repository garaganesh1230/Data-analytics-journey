# Problem: Find maximum element in array

# -----------------------------------
# Static Input
arr = [10, 20, 5, 40, 15]

# Dynamic Input (optional)
# arr = list(map(int, input("Enter numbers: ").split()))
# -----------------------------------

# Logic
maximum = arr[0]

for num in arr:
    if num > maximum:
        maximum = num

# Output
print("Maximum element:", maximum)
