# Problem: Reverse an array

# Static input
arr = [1, 2, 3, 4, 5]

# Dynamic input (optional)
# arr = list(map(int, input("Enter numbers: ").split()))

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("Reversed array:", arr)
