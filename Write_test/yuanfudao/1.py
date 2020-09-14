n, time = list(map(int, input().split()))
nums = list(map(int, input().split()))

beginindex = [i for i in range(n)]


def change(indexinput):
    resultindex = []
    for i in indexinput:
        resultindex.append((i*2) % (n+1))
    return resultindex


indexlists = []
curindex = [i+1 for i in range(n)]
for i in range(10):
    indexlists.append(change(curindex))
    curindex = indexlists[-1]


def indexread(resindex, ref):
    tempres = [0 for i in range(n)]
    for index, i in enumerate(ref):
        tempres[i-1] = resindex[index]
    return tempres


resultindex = [i+1 for i in range(n)]

result = nums
cur = 0
while time:
    if time & 1:
        result = indexread(result, indexlists[cur])
    time = time//2
    cur += 1

print(' '.join(map(str, result)))
