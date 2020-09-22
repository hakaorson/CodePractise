'''
3 2 3
1 2
2 3
3 2
2 1
1 3
'''

n, m, q = list(map(int, input().split()))
links, search = [], []
roots = [-1 for i in range(n)]


def findroot(roots, target):
    while roots[target] != -1:
        target = roots[target]
    return target


for i in range(m):
    a, b = list(map(int, input().split()))
    aroot = findroot(roots, a-1)
    broot = findroot(roots, b-1)
    if aroot != broot:
        roots[broot] = aroot


for i in range(q):
    a, b = list(map(int, input().split()))
    aroot = findroot(roots, a-1)
    broot = findroot(roots, b-1)
    if aroot != broot:
        print('NO')
    else:
        print('YES')
