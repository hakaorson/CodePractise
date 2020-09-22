n, m, r = list(input().split())
# 7495417.6435616808 10 6125201.7312234128
n = float(n)
r = float(r)
m = int(m)

cur = 0.00
situ = 0


def printsitu(situ, num):
    if situ == 0:
        nums = [num, 0.00]
    elif situ == 1:
        nums = [n, num]
    elif situ == 2:
        nums = [n-num, n]
    else:
        nums = [0.00, n-num]
    print('%.2f' % nums[0], ' ', '%.2f' % nums[1])


for mi in range(m):
    cur = cur+r
    if cur > n:
        time = int(cur/n)
        situ = (situ+time) % 4
        cur = cur-n*time
    printsitu(situ, cur)
