n, multi = list(map(int, input().split()))
nums = list(map(int, input().split()))
doublenums = nums+nums


def findmax(nums):
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    maxresult = dp[0]
    maxleft, maxtight = 0, 0
    pre = 0
    for i in range(1, len(nums)):
        if dp[i-1] < 0:
            pre = i
            dp[i] = nums[i]
        else:
            dp[i] = dp[i-1]+nums[i]
        if dp[i] >= maxresult:
            maxresult = dp[i]
            maxleft = pre
            maxtight = i+1
    return maxresult, maxleft, maxtight


singlemax, _, _ = findmax(nums)
if multi == 1:
    print(singlemax)
else:
    doublemax, left, right = findmax(doublenums)
    if left < n and right >= n:
        result = doublemax+max(sum(nums), 0)*(multi-2)
        print(result)
    else:
        print(singlemax)


# findmax([1, 3, -9, 2, 4, 1, 3, -9, 2, 4])
