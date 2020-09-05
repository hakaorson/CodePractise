m, n = list(map(int, input().split()))
left = 0
right = n-1
low = 0
up = m-1


def is_ok(index):
    stri = str(index)
    if len(stri) >= 2 and stri[-1] == '7' and int(stri[-2]) % 2 == 1:
        return True
    else:
        return False
# 79 11 82 75 44

index = 0
res = []
while True:
    for i in range(left, right+1):
        index += 1
        if is_ok(index):
            res.append([low, i])
    low += 1
    if low > up:
        break

    for i in range(low, up+1):
        index += 1
        if is_ok(index):
            res.append([i, right])
    right -= 1
    if right < left:
        break
    for i in range(right, left-1, -1):
        index += 1
        if is_ok(index):
            res.append([up, i])
    up -= 1
    if up < low:
        break
    for i in range(up, low-1, -1):
        index += 1
        if is_ok(index):
            res.append([i, left])
    left += 1
    if left > right:
        break
tempres = str(res)
print(tempres.replace(" ", ""))
