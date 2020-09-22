'''
3
3 3
###
#@*
***
3 4
####
#@.*
**.*
3 3
.#.
#@#
.#.
'''
import queue

k = int(input())
for ki in range(k):
    m, n = list(map(int, input().split()))
    home = []
    for mi in range(m):
        inputstr = list(input())
        if '@' in inputstr:
            curi = mi
            curj = inputstr.index('@')
        home.append(inputstr)
    matrix = [[m+n for j in range(n)]for i in range(m)]
    matrix[curi][curj] = 0

    curqueue = queue.Queue()
    curqueue.put([curi, curj])
    res = m+n
    while not curqueue.empty():
        curi, curj = curqueue.get()
        if curi == 0 or curi == m-1 or curj == 0 or curj == n-1:
            res = min(res, matrix[curi][curj])
        for diri, dirj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            tempi = curi+diri
            tempj = curj+dirj
            if tempi < 0 or tempi >= m or tempj < 0 or tempj >= n or home[tempi][tempj] == '#':
                pass
            elif home[tempi][tempj] == '.':
                if matrix[tempi][tempj] > matrix[curi][curj]:
                    matrix[tempi][tempj] = matrix[curi][curj]
                    curqueue.put([tempi, tempj])
            else:
                if matrix[tempi][tempj] > matrix[curi][curj]+1:
                    matrix[tempi][tempj] = matrix[curi][curj]+1
                    curqueue.put([tempi, tempj])
    if res == m+n:
        print(-1)
    else:
        print(res)
