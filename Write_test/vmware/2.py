'''
2
5
1 2 3 4 5
1 1 3 3 5
10
10 2 9 8 3 6 7 1 4 5
2 8 6 6 6 6 5 5 5 5
'''
n = int(input())
for ni in range(n):
    size = int(input())
    homes = list(map(int, input().split()))
    color = list(map(int, input().split()))
    homeindex = 0
    cindex = 0
    suc = False
    while(homeindex < size):
        if (homes[homeindex] != color[cindex]):
            homeindex += 1
            continue
        homeindex += 1
        cindex += 1
        while(cindex < size and color[cindex] == color[cindex-1]):
            cindex += 1
        if cindex == size:
            suc = True
            break
    if suc:
        print('YES')
    else:
        print('NO')
