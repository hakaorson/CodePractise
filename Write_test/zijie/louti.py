n = int(input())
dpmaxritx = [[0, 0, 0]for i in range(n+1)]
dpmaxritx[0][0] = 1
for i in range(1, n+1):
    dpmaxritx[i][1] = dpmaxritx[i-1][0] + dpmaxritx[i-1][1]+dpmaxritx[i-1][2]
    if i > 1:
        dpmaxritx[i][2] = dpmaxritx[i-2][0] + dpmaxritx[i-2][1]
for i in range(len(dpmaxritx)):
    print(i, " ", sum(dpmaxritx[i]))
print(sum(dpmaxritx[-1]))
