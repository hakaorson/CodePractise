# n,m = list(map(int, input().split()))
n = 36
m = 6
#三维dp解决跳台阶问题

matrix = [[[0 for k in range(m+1)]for j in range(m+1)]for i in range(n+1)]
for i in range(1, n+1):
    for firstjump in range(0, m+1):
        for secondjump in range(1, m+1):
            if firstjump != secondjump:
                if i == firstjump+secondjump:
                    matrix[i][firstjump][secondjump] = 1
                elif firstjump != 0:
                    for prejump in range(0, m+1):
                        if i-secondjump >= prejump+firstjump and prejump != firstjump and prejump != secondjump:
                            matrix[i][firstjump][secondjump] += matrix[i -
                                                                    secondjump][prejump][firstjump]
                else:
                    pass
result = 0
for i in matrix[-1]:
    result += sum(i)
print(result)
