# 7 3 1 4
#10 20 2 29 ——20+29
nums = list(map(int, input().split()))

nums2 = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
res = 0
for num in nums:
    if num % 7 == 0:
        res += num
    else:
        res += (num//7)*7
        nums2[num % 7] += 1

for i in range(1, 4):
    minnum = min(nums2[i], nums2[7-i])
    nums2[i] -= minnum
    nums2[7-i] -= minnum
    res += 7*minnum
if res==0:
    print(-1)
else:
    print(res)
