s = input()
dp_matrix = [[True for j in range(len(s))]for i in range(len(s))]
for i in range(len(s)-2, -1, -1):
    for j in range(i+1, len(s)):
        if not (s[i] == s[j] and dp_matrix[i+1][j-1]):
            dp_matrix[i][j] = False
n = int(input())
for i in range(n):
    l, r = list(map(int, input().split()))
    l -= 1
    result = 0
    while dp_matrix[l][r-1] == False:
        lastture = l
        for i in range(l, r):
            if dp_matrix[l][i] is True:
                lastture = i
        result += 1
        l = lastture+1
    result += 1
    print(result)
