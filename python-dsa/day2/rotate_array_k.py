# Problem: Rotate array to the right by K positions

# Sample Input:
# Array: 1 2 3 4 5
# K = 2

# Sample Output:
# [4, 5, 1, 2, 3]


arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter K: "))

n = len(arr)

# Handle cases where k > n
k = k % n

# Logic (Right Rotation)
rotated = arr[-k:] + arr[:-k]

# Output
print("Rotated array:", rotated)
