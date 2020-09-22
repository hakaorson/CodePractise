# 92
n = 8
nums = [-1 for i in range(n)]
res = 0


def dfs(nums, cur):
    global res
    if cur == n:
        res += 1
        # print(nums)
        return
    choose = [i for i in range(n)]
    for index, num in enumerate(nums[0:cur]):
        choose[num] = -1
        if num-(cur-index) >= 0:
            choose[num-(cur-index)] = -1
        if num+(cur-index) < n:
            choose[num+(cur-index)] = -1
    for ch in choose:
        if ch != -1:
            nums[cur] = ch
            dfs(nums, cur+1)
    return


dfs(nums, 0)

pass
