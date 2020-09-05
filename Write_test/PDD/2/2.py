m, n = list(map(int, input().split()))
nums=[]
sums=0
for i in range(m):
    temp=list(map(int, input().split()))
    nums.append(temp)
    sums+=sum(temp)
print(sums)
