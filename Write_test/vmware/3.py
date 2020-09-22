'''
4 4
1 2
2 3
1 4
1 3
'''

n, k = list(map(int, input().split()))
matrix = [0 for i in range(n+1)]
chooses = {}
for ki in range(k):
    i, j = list(map(int, input().split()))
    i, j = min(i, j), max(i, j)
    matrix[i] += 1
    matrix[j] += 1
    if (i, j) in chooses.keys():
        chooses[(i, j)] += 1
    else:
        chooses[(i, j)] = 1
res = 0
for i in range(1, n+1):
    for j in range(i+1, n+1):
        if matrix[i]+matrix[j] >= k:
            sums = matrix[i]+matrix[j]
            if (i, j) in chooses.keys():
                sums -= chooses[(i, j)]
            if sums >= k:
                res += 1
print(res)
