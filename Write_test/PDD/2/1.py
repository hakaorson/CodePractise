# nums = list(map(int, input().split()))
# cars = sorted(nums, key=lambda x: x[0], reverse=1)


n = int(input())
size = n//2
result = [[0 for j in range(n)]for i in range(n)]

mapping = {
    (1, -1, 1, 1): 1,
    (1, 1, 1, 1): 2,
    (1, 1, 1, -1): 3,
    (-1, 1, 1, -1): 4,
    (-1, 1, -1, -1): 5,
    (-1, -1, -1, -1): 6,
    (-1, -1, -1, 1): 7,
    (1, -1, -1, 1): 8
}


def up(i, j):
    if i < size:
        return 1
    elif i>=n-size:
        return -1
    else:
        return 0


def left(i, j):
    if j < size:
        return 1
    elif j>=n-size:
        return -1
    else:
        return 0


def lu(i, j):
    if i+j < n-1:
        return 1
    elif i+j>n-1:
        return -1
    else:
        return 0


def ru(i, j):
    if j > i:
        return 1
    elif j<i:
        return -1
    else:
        return 0


for i in range(n):
    for j in range(n):
        tempkey = (up(i, j), left(i, j), lu(i, j), ru(i, j))
        if tempkey in mapping.keys():
            result[i][j] = mapping[tempkey]

for nums in result:
    tempstr=" ".join(map(str,nums))
    print(tempstr)
