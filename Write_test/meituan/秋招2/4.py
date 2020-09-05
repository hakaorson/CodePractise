n,m=list(map(int, input().split()))
nums = list(map(int, input().split()))
nums = [0]+nums+[m]
revnums = reversed(nums)
maxindexlessthan = [0 for i in range(m+1)]
minindexmorethan = [len(nums)-1 for i in range(m+1)]

for target in range(1, m+1):
    minnum = nums[0]
    for index in range(1, len(nums)):
        if nums[index] >= target:
            continue
        if nums[index] < minnum:
            maxindexlessthan[target] = -1
            break
        else:
            minnum = nums[index]
            maxindexlessthan[target] = index
for target in range(m, 0, -1):
    maxnum = nums[-1]
    for index in range(len(nums)-2, -1, -1):
        if nums[index] <= target:
            continue
        if nums[index] > maxnum:
            minindexmorethan[target] = -1
            break
        else:
            maxnum = nums[index]
            minindexmorethan[target] = index
result = 0
for l in range(1, m+1):
    for r in range(l, m+1):
        if maxindexlessthan[l] == -1 or minindexmorethan[r] == -1:
            continue
        if maxindexlessthan[l] >= minindexmorethan[r]:
            continue
        result += 1
print(result)
