'''
5
1 5 3 4 2 
2 3 5 4 1 
5 4 1 2 3 
1 2 5 4 3 
1 4 5 2 3
'''
n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
choosed = []


temp = [False for i in range(n)]
for i in range(n):
    for index in choosed:
        temp[matrix[i][index-1]-1] = True
    candidate = temp.index(False)
    choosed.append(matrix[i].index(candidate+1)+1)
result=" ".join(list(map(str,choosed)))
print(result)

pass
