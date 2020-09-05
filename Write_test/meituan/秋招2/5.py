# 5
# 7 6 5 1 3

# n = int(input())
# nums = list(map(int, input().split()))
n = 5
nums = [7, 6, 5, 1, 3]
result = sum(nums)*len(nums)


def dfs(nums, h):
    global result
    if len(nums) == 0:
        return 0
    for choose in range(len(nums)):
        cur = nums[choose]*h
        temp = cur+sum(nums[0:choose])*(h+1) + \
            sum(nums[choose+1:len(nums)])*(h+1)
        if temp >= result:
            continue
        left = dfs(nums[0:choose], h+1)
        right = dfs(nums[choose+1:len(nums)], h+1)
        result = min(result, cur+left+right)
    return result


dfs(nums, 0)
print()
