nums = list(map(int, input().split()))
res = nums[0]
count = 1
for i in range(1, len(nums)):
    if nums[i] == res:
        count += 1
    else:
        count -= 1
        if count == 0:
            res = nums[i]
            count = 1
print(res)
