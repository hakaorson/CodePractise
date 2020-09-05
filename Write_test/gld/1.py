n = 5
nums = [3, 3, 5, 1, 1, 1, 1, 4, 4, 4]
n = int(input())
nums = list(map(int, input().split(' ')))

mapping = {}
for num in nums:
    if num in mapping.keys():
        mapping[num] += 1
    else:
        mapping[num] = 1
newnums = []
for num in mapping.keys():
    if mapping[num] in [2, 3]:
        newnums.append(num)
    elif mapping[num] >= 4:
        newnums.append(num)
        newnums.append(num)
    else:
        pass
if sum(newnums) < 2:
    print(-1)
result = 0
current1 = 0
current2 = 0
for num in newnums:
    if num > current1:
        if num > current2:
            current1 = current2
            current2 = num
        else:
            current1 = num
print(current1*current2)
