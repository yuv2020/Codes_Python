def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return None

# Test case
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
if result:
    print(f"The indices of the two numbers that add up to the target are: {result}")
    print(f"The numbers are {nums[result[0]]} and {nums[result[1]]}")
else:
    print("No two numbers add up to the target.")
