'''
hello , 
I am a coder
hello ,  I am a singer
'''
strsNoConsider = set(list(input().split()))
strsFirst = [""] + list(input().split())
strsSecond = [""] + list(input().split())

sizeFirst = len(strsFirst)
sizeSecond = len(strsSecond)
matrix = [[0 for j in range(sizeSecond)]for i in range(sizeFirst)]
temp = 0
for i in range(1, sizeFirst):
    if strsFirst[i] not in strsNoConsider:
        temp += 1
    matrix[i][0] = temp
temp = 0
for j in range(1, sizeSecond):
    if strsSecond[j] not in strsNoConsider:
        temp += 1
    matrix[0][j] = temp


for i in range(1, sizeFirst):
    for j in range(1, sizeSecond):
        if strsFirst[i] == strsSecond[j]:
            matrix[i][j] = matrix[i-1][j-1]
        else:
            matrix[i][j] = 1+min(matrix[i-1][j], matrix[i]
                                 [j-1], matrix[i-1][j-1])
            if strsFirst[i] in strsNoConsider:
                matrix[i][j] = min(matrix[i][j], matrix[i-1][j])
            if strsSecond[j] in strsNoConsider:
                matrix[i][j] = min(matrix[i][j], matrix[i][j-1])
print(matrix[-1][-1])
