n = int(input())
lists = []
for i in range(n):
    lists.append(int(input()))


def subsort(lists):
    if len(lists) == 0:
        return [-1, -1]
    leftcur = 0
    leftmax = lists[0]-1
    rightcur = len(lists)-1
    rightmin = lists[len(lists)-1]+1
    while leftmax <= lists[leftcur]:
        leftmax = lists[leftcur]
        leftcur += 1
        if leftcur == len(lists):
            return [-1, -1]
    while rightmin >= lists[rightcur]:
        rightmin = lists[rightcur]
        rightcur -= 1
    rightmax = rightmin
    for i in range(rightcur, -1, -1):
        if lists[i] >= rightmax:
            rightmax = lists[i]
    leftmin = leftmax
    for i in range(leftcur, len(lists)):
        if lists[i] <= leftmin:
            leftmin = lists[i]
    finalrightindex = len(lists)-1
    while lists[finalrightindex] >= rightmax:
        finalrightindex -= 1
    finalleftindex = 0
    while lists[finalleftindex] <= leftmin:
        finalleftindex += 1
    return [finalleftindex, finalrightindex]


result = subsort(lists)
print(result[0])
print(result[1])
