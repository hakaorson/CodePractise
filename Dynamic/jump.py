n = int(input())
if n < 1:
    print(-1)
elif n == 1:
    print(1)
elif n>36:
    print(-1)
else:
    matrix = [0 for i in range(n+1)]
    matrix[0] = 1
    for i in range(1, n+1):
        matrix[i] = matrix[i-1]+matrix[i-2]
    print(matrix[-1] % int(1e9+7))
