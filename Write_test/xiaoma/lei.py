# n = 1
# size = 3
# datas = [[1, -1, 1], [-1, 2, -1], [1, -1, 1]]


def check(datas, to_be_check, res):
    if len(to_be_check) == 0:
        return res+1
    i, j = to_be_check.pop()
    chooses = [0, 1] if i != 1+size else [0]
    temp_res = 0
    for choose in chooses:
        datas[i][j] = choose
        if i >= 2:
            if datas[i-1][j] == datas[i][j]+datas[i-2][j]+datas[i-1][j-1]+datas[i-1][j+1]:
                temp_res += check(datas, to_be_check, res)
        else:
            temp_res += check(datas, to_be_check, res)
        datas[i][j] = -1
    return temp_res


n = int(input())
for _ in range(n):
    size = int(input())
    datas = []
    datas.append([0 for _ in range(size+2)])
    for i in range(size):
        temp_data = '0 ' + input().replace('?', '-1') + ' 0'
        temp_data = list(map(int, temp_data.split(' ')))
        datas.append(temp_data)
    datas.append([0 for _ in range(size+2)])
    to_be_check = []
    for i in range(1, 2+size):
        for j in range(1, 1+size):
            if (i+j) % 2:
                to_be_check.append([i, j])
    to_be_check.reverse()
    res = check(datas, to_be_check, 0)
    a = 1
    pass


'''
1
3
1 ? 1
? 2 ?
1 ? 1
'''
