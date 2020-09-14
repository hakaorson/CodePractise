'''
hello , 
I am a coder
hello ,  I am a singer
'''
strsNoConsider = set(list(input().split()))
strsFirst = [""] + list(input().split())
strsSecond = [""] + list(input().split())

strsFirstTemp = []
for i in strsFirst:
    if i not in strsNoConsider:
        strsFirstTemp.append(i)
strsFirst = strsFirstTemp

strsSecondTemp = []
for i in strsSecond:
    if i not in strsNoConsider:
        strsSecondTemp.append(i)
strsSecond = strsSecondTemp

sizeFirst = len(strsFirst)
sizeSecond = len(strsSecond)
matrix = [[0 for j in range(sizeSecond)]for i in range(sizeFirst)]
for j in range(sizeSecond):
    matrix[0][j] = j

for i in range(sizeFirst):
    matrix[i][0] = i

for i in range(1, sizeFirst):
    for j in range(1, sizeSecond):
        if strsFirst[i] == strsSecond[j]:
            matrix[i][j] = matrix[i-1][j-1]
        else:
            matrix[i][j] = 1+min(matrix[i-1][j], matrix[i]
                                 [j-1], matrix[i-1][j-1])
print(matrix[-1][-1])
