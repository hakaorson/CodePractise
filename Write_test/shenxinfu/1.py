n = int(input())
nums = list(map(int, input().split()))
minnum = min(nums)
print(sum(nums)-minnum*len(nums))
