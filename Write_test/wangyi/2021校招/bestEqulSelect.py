n = int(input())
for _ in range(n):
    lenght = int(input())
    nums = list(map(int, input().split()))
    # nums = [30, 60, 5, 15, 30]
    maxnum = sum(nums)//2
    situEXit = [[False for j in range(maxnum)] for i in range(maxnum)]
    situEXit[0][0] = True
    for num in nums:
        for i in range(maxnum-1, -1, -1):
            for j in range(maxnum-1, -1, -1):
                if (i >= num and situEXit[i-num][j])or (j >= num and situEXit[i][j-num]):
                    situEXit[i][j] = True
    for index in range(maxnum-1, -1, -1):
        if situEXit[index][index]:
            print(sum(nums)-index*2)
            break

