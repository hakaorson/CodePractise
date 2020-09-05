# m, n = list(map(int, input().split()))
m = 10
n = 10
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

index = 7
begin = 6
res = []
while True:
    while begin <= right-left:
        if is_ok(index):
            res.append([low, begin+left])
        begin += 10
        index += 10
    begin = begin - 1 - (right-left)
    low += 1
    if low > up:
        break
    while begin <= up-low:
        if is_ok(index):
            res.append([begin+low, right])
        begin += 10
        index += 10
    begin = begin - 1 - (up-low)
    right -= 1
    if right < left:
        break
    while begin <= right-left:
        if is_ok(index):
            res.append([up, right-begin])
        begin += 10
        index += 10
    begin = begin - 1 - (right-left)
    up -= 1
    if up < low:
        break
    while begin <= (up-low):
        if is_ok(index):
            res.append([up-begin, left])
        begin += 10
        index += 10
    begin = begin - 1 - (up-low)
    left += 1
    if left > right:
        break
tempres = str(res)
print(tempres.replace(" ", ""))
