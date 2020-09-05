nums = list(map(int, input().split()))
others = list(map(int, input().split()))
othersset = set(others)
othersmap = {}
for num in nums:
    if num in othersset:
        if num not in othersmap.keys():
            othersmap[num] = 1
        else:
            othersmap[num] += 1
result = []
for num in others:
    for i in range(othersmap[num]):
        result.append(num)
result2 = []
for num in nums:
    if num not in othersmap.keys():
        result2.append(num)
result2.sort()
result.extend(result2)
result = list(map(str, result))
print(" ".join(result))
