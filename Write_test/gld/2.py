n = 4
nums = [2, 1, 3, 4, 2]

n = int(input())
nums = list(map(int, input().split(' ')))
max_num = nums[0]
result = 0
for num in nums:
    if num < max_num:
        result += 1
    else:
        max_num = num
print(result)
