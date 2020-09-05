n = 4
nums = [1, 0, 2, 2]
n = input()
nums = list(map(int, input().split()))
nums = sorted(nums)
statics = [0 for i in range(nums[-1]+1)]
for num in nums:
    statics[num] += 1
tempforC = {}
result = 1
for index, choose in enumerate(statics):
    if index == 0:
        continue
    cur = (statics[index-1]*2, min(statics[index-1]*2-choose, choose))
    temp_beishu = 1
    if cur in tempforC.keys():
        temp_beishu = tempforC[cur]
    else:
        for i in range(choose):
            temp_beishu *= (statics[index-1]*2-i)
        for i in range(choose):
            temp_beishu //= (i+1)
        tempforC[cur] = temp_beishu
    result *= temp_beishu
print(result % int(1e9+7))


pass
