nums = [[0, 0, 1, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0]]


def findmax(nums):
    import queue
    que = queue.Queue()
    m, n = len(nums), len(nums[0])
    mask = [[False for j in range(n)]for i in range(m)]
    res = 0
    for i in range(m):
        for j in range(n):
            if nums[i][j] and mask[i][j] is False:
                que.put((i, j))
                mask[i][j] = True
                size = 1
                while not que.empty():
                    curi, curj = que.get()
                    neibors = [(curi-1, curj), (curi, curj-1),
                               (curi+1, curj), (curi, curj+1)]
                    for neii, neij in neibors:
                        if 0 <= neii < m and 0 <= neij < n and nums[neii][neij] and not mask[neii][neij]:
                            que.put((neii, neij))
                            mask[neii][neij] = True
                            size += 1
                res = max(res, size)
    return res


findmax(nums)
