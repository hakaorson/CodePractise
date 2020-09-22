'''
3 10
2 2 3
1 5 10
2 4 12
'''
n, p = list(map(int, input().split()))
goods = [[0, 0, 0]]
for i in range(n):
    goods.append(list(map(int, input().split())))


matrix = [[0 for j in range(p+1)]for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, p+1):
        maxres, k = 0, 0
        goodsinfo = goods[i]
        while k <= goodsinfo[0] and k*goodsinfo[1] <= j:
            tempres = matrix[i-1][j-k*goodsinfo[1]]+k*goodsinfo[2]
            maxres = max(maxres, tempres)
            k += 1
        matrix[i][j] = maxres
print(matrix[-1][-1])
