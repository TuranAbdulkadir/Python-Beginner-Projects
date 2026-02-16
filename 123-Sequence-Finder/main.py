# Number Sequence Finder
nums = input("Enter numbers (comma separated): ").split(",")
nums = [int(n.strip()) for n in nums]
diffs = [nums[i+1] - nums[i] for i in range(len(nums)-1)]
if len(set(diffs)) == 1:
    next_val = nums[-1] + diffs[0]
    print(f"Arithmetic sequence (d={diffs[0]})")
    print(f"Next value: {next_val}")
elif len(nums) >= 3:
    ratios = [nums[i+1] / nums[i] for i in range(len(nums)-1) if nums[i] != 0]
    if len(set(round(r, 4) for r in ratios)) == 1:
        print(f"Geometric sequence (r={ratios[0]:.2f})")
        print(f"Next value: {nums[-1] * ratios[0]:.0f}")
    else:
        print(f"Pattern not recognized")
        print(f"Differences: {diffs}")
