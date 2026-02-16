# Selection Sort
import time
data = [29, 10, 14, 37, 13, 25, 44, 8, 31, 19]
print(f"Original: {data}\n")
n = len(data)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if data[j] < data[min_idx]:
            min_idx = j
    data[i], data[min_idx] = data[min_idx], data[i]
    print(f"Step {i+1}: {data}")
    time.sleep(0.2)
print(f"\nSorted: {data}")
