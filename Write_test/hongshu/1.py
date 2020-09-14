'''
2
3
3 1 4
5 8 10
'''

n = int(input())
m = int(input())
maxnum = 0
nums = []
for i in range(n):
    temp = list(map(int, input().split()))
    nums.append(temp)
    maxnum = max(maxnum, max(temp))
result = [False for i in range(maxnum+2)]
for i in range(n):
    for j in range(m):
        result[nums[i][j]] = True
find = False
for i in range(1, maxnum+2):
    if result[i] is False:
        print(i)
        break
