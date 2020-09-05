n = int(input())
nums = list(map(int, input().split()))


def dfs(l, r):
    curmin = min(nums[l: r+1]) if r+1 > l else nums[l]
    for i in range(l, r+1):
        nums[i] -= curmin
    start = l
    tempsum = curmin
    for i in range(l, r+1):
        if nums[i] != 0:
            start = i
            break
    for i in range(start, r+1):
        if nums[i] == 0:
            tempsum += dfs(start, i-1)
            start = i+1
    if start <= r:
        tempsum += dfs(start, r)
    return min(tempsum, r-l+1)


result = dfs(0, len(nums)-1)
print(result)
