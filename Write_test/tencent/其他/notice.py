n, m = list(map(int, input().split()))

fa = [i for i in range(n+1)]


def getFather(x):
    if x != fa[x]:
        fa[x] = getFather(fa[x])
        return fa[x]
    return x


def mergeFather(x, y):
    fx, fy = getFather(x), getFather(y)
    if fx == fy:
        return False
    if fx > fy:
        fx, fy = fy, fx
    fa[fx] = fy
    return True


for _ in range(m):
    arr = list(map(int, input().split()))
    if arr[0] >= 2:
        for i in range(2, arr[0] + 1):
            mergeFather(arr[1], arr[i])

ans, root = 0, getFather(0)
for i in range(n+1):
    if getFather(i) == root:
        ans += 1

print(ans)
