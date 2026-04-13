# Problem: Find frequency of each element in an array

# Sample Input:
# 1 2 2 3 1 2

# Sample Output:
# 1 : 2
# 2 : 3
# 3 : 1

# Dynamic Input
arr = list(map(int, input("Enter numbers: ").split()))

# Logic
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Output
for key, value in freq.items():
    print(key, ":", value)
