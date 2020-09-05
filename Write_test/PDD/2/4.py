n, size = list(map(int, input().split()))
nums = []
for i in range(size):
    nums.append(int(input()))

numselect = [False for i in range(21)]


def gysgs(m, n):
    m, n = max(m, n), min(m, n)
    mnew = m
    nnew = n
    while n != 0:
        temp = m % n
        m = n
        n = temp
    return mnew*nnew//m


def getnum(i):
    if i > n:
        return 0
    mini = i
    maxi = n-n % i
    size = (maxi-mini)//i+1
    return size


result = 0
loop = 1
for i in range(len(nums)):
    loop = gysgs(loop, nums[i])

loopres = 0
for i in range(1, loop+1):
    isin = False
    for j in nums:
        if isin == False and i % j == 0:
            loopres += 1
            isin = True

beishu = n//loop

finalresult = beishu*loopres
for i in range(n % loop):
    i+=1
    isin = False
    for j in nums:
        if isin == False and i % j == 0:
            finalresult += 1
            isin = True
print(finalresult)
#     result += getnum(nums[i])
#     for i in range(1,21):
#         if i%nums[i]==0:
#             numselect[i]=True
#     for j in range(i):
#         gcd = gysgs(nums[i], nums[j])
#         result -= getnum(gcd)
# print(result % int(1e9+7))
