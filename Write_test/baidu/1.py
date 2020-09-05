# nums = list(map(int, input().split()))
# cars = sorted(nums, key=lambda x: x[0], reverse=True)
n = int(input())
for i in range(n):
    length, size = list(map(int, input().split()))
    nums = []
    for i in range(size):
        l, r = list(map(int, input().split()))
        nums.append([l-1, r-l+1])
    situation=[]
    nums.sort(key=lambda x: x[0])
    numscur=0
    result=[]
    i=0
    while i<length:
        if len(situation)==0:
            nexttarget=nums[numscur][0] if numscur<len(nums) else length
            icopy=i
            for k in range(nexttarget-icopy):
                result.append(0)
                i+=1
        while numscur<len(nums) and nums[numscur][0]==i:
            situation.append(nums[numscur][1])
            numscur+=1
        result.append(len(situation))
        i+=1
        # minnum=min(situation) if len(situation) else 0
        # truenum=0
        # for j in range(minnum):
        #     result.append(len(situation))
        #     i+=1
        #     truenum+=1
        #     if numscur<len(nums) and i==nums[numscur][0]:
        #         break
        newsitu=[]
        for j in situation:
            if j-1:
                newsitu.append(j-1)
        situation=newsitu
    print(" ".join(map(str,result)))
    pass
'''
2
6 3
1 2
4 5
4 5
6 3
1 2
4 5
4 5
'''