# Bubble Sort Visualizer
import time
data = [64, 34, 25, 12, 22, 11, 90, 45, 78, 33]
print(f"Original: {data}\n")

def bubble_sort(arr):
    n = len(arr)
    step = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                step += 1
                bar = " ".join(f"[{x:2d}]" for x in arr)
                print(f"Step {step:2d}: {bar}")
                time.sleep(0.1)
    return step

steps = bubble_sort(data)
print(f"\nSorted: {data}")
print(f"Total swaps: {steps}")
