nums = list(map(int, input().split()))
n = len(nums)
nums.sort()
ans = list()

for first in range(n):
    if first > 0 and nums[first] == nums[first - 1]:
        continue
    third = n - 1
    target = -nums[first]
    for second in range(first + 1, n):
        if second > first + 1 and nums[second] == nums[second - 1]:
            continue
        while second < third and nums[second] + nums[third] > target:
            third -= 1
        if second == third:
            break
        if nums[second] + nums[third] == target:
            print(" ".join(map(str, [nums[first],nums[second],nums[third]])))
