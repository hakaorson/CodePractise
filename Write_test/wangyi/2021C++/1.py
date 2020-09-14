n = int(input())
strs = []
for i in range(n):
    strs.append(list(input().split()))


def dfs(pos, cur: list):
    if pos >= 0:
        for k in range(len(strs[pos])):
            cur.append(k)
            dfs(pos-1, cur)
            cur.pop(-1)
    else:
        cur.reverse()
        res = '-'.join(strs[index][select] for index, select in enumerate(cur))
        print(res)
        cur.reverse()


dfs(n-1, [])
