# Temperature Logger
temps = []
print("=== Temperature Logger ===")
while True:
    t = input("Enter temp (or 'done'): ")
    if t.lower() == "done": break
    temps.append(float(t))
if temps:
    print(f"\nReadings: {len(temps)}")
    print(f"Average: {sum(temps)/len(temps):.1f}°")
    print(f"Max: {max(temps)}°")
    print(f"Min: {min(temps)}°")
    print(f"Range: {max(temps)-min(temps):.1f}°")
