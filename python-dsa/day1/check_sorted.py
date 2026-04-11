# Problem: Check if array is sorted

# -----------------------------------
# Static Input
arr = [1, 2, 3, 4, 5]

# Dynamic Input (optional)
# arr = list(map(int, input("Enter numbers: ").split()))
# -----------------------------------

# Logic
is_sorted = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break

# Output
if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")
