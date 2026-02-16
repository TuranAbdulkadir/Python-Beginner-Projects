# File Statistics Analyzer
import os
path = input("Enter file path: ")
if os.path.isfile(path):
    size = os.path.getsize(path)
    with open(path, 'r', errors='ignore') as f:
        content = f.read()
    lines = content.count('\n') + 1
    words = len(content.split())
    chars = len(content)
    print(f"\nFile: {os.path.basename(path)}")
    print(f"Size: {size:,} bytes")
    print(f"Lines: {lines:,}")
    print(f"Words: {words:,}")
    print(f"Characters: {chars:,}")
    print(f"Avg words/line: {words/lines:.1f}")
else:
    print("File not found!")
