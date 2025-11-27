import time
t = int(input("Seconds: "))
while t:
    print(t)
    time.sleep(1)
    t -= 1
print("Time Up!")