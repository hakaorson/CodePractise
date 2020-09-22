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


def compute(matrix, visited, home):
    pass


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
    visited = [[False for j in range(n)]for i in range(m)]

    curqueue = queue.Queue()
    curqueue.put([curi, curj])
    while not curqueue.empty():
        curi, curj = curqueue.get()
        visited[curi][curj] = True
        if curi == 0 or curi == m-1 or curj == 0 or curj = n-1:
            print(matrix[curi][curj])
            break
        for diri, dirj in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            tempi = curi+diri
            tempj = curj+dirj
            if home[tempi][tempj] == '#':
                pass
            elif home[tempi][tempj] == '.':
                if matrix[tempi][tempj]>matrix[curi][curj]:
                    matrix[tempi][tempj]=matrix[curi][curj]
                    cur
            else:
                matrix[tempi][tempj] = min(
                    matrix[tempi][tempj], matrix[curi][curj]+1)
    
