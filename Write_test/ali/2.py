n = 44444442
m = 4
yushu = [[0 for _ in range(16)]for _ in range(10)]

for i in range(10):
    for j in range(16):
        yushu[i][j] = (i*pow(10, j)) % m
status = list(map(int, list(str(n))))
status.sort()
leght = len(status)

result = 0


def dfs(cutstatus, cutyushu):
    if len(cutstatus) == 0:
        if cutyushu == 0:
            return 1
        else:
            return 0
        return
    if len(cutstatus) == 1 and cutstatus[0] == 0:
        return 0
    tempresult = 0
    pre = -1
    for index in range(len(cutstatus)):
        if pre == -1 or pre != cutstatus[index]:
            pre = cutstatus[index]
            cutyushu += yushu[cutstatus[index]][leght-len(cutstatus)]
            temp = cutstatus[0:index]+cutstatus[index+1:len(cutstatus)]
            tempresult += dfs(temp, cutyushu % m)
            cutyushu -= yushu[cutstatus[index]][leght-len(cutstatus)]
    return tempresult


final = dfs(status, 0)

pass
