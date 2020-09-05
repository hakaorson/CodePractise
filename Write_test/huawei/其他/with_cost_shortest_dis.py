K = int(input())
N = int(input())
R = int(input())
matx = [[0 for i in range(N+1)] for j in range(N+1)]
cost = [[0 for i in range(N+1)] for j in range(N+1)]
dp = [[100000000 for i in range(K+1)] for j in range(N+1)]
inque = [[False for i in range(K+1)] for j in range(N+1)]
for i in range(R):
    S, D, L, T = map(int, input().strip().split())
    matx[S][D] = L
    cost[S][D] = T
dp[1][0] = 0
q = [[1,0]]
h = 0
while h<len(q):
    cur, cst = q[h]
    for i in range(1, N+1):
        ncst = cst+cost[cur][i]
        if (matx[cur][i]==0 or i==cur or ncst>K):
            continue
        if dp[i][ncst]>dp[cur][cst]+matx[cur][i]:
            dp[i][ncst] = dp[cur][cst]+matx[cur][i]
            if not inque[i][ncst]:
                q.append([i, ncst])
                inque[i][ncst] = True
    h+=1

ans = 100000000
for i in range(K+1):
    ans = min(ans, dp[N][i])

print(ans if ans<100000000 else -1)