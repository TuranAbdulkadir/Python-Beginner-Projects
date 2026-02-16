# Binary Search
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    steps = 0
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        print(f"  Step {steps}: checking index {mid} (value={arr[mid]})")
        if arr[mid] == target: return mid, steps
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1, steps

data = sorted([3,7,11,15,22,28,35,42,50,61,73,88,95])
print(f"Array: {data}")
target = int(input("Search for: "))
idx, steps = binary_search(data, target)
if idx != -1: print(f"\nFound at index {idx} in {steps} steps")
else: print(f"\nNot found ({steps} steps)")
