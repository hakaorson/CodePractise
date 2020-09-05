'''
有一个初始的数，在一个数组中循环的减去当前这个值（如果可以的话），直到无法继续
'''


m = 4
n = 24
nums = [2, 1, 4, 3]
'''
m, n = list(map(int, input().split()))
nums = list(map(int, input().split()))
'''
sums = sum(nums)
result = (n//sums)*m
lefted = n-result//m*sums
temp_num = nums
while(lefted):  # 需要注意另一个退出条件，就是当前的数太小了
    replace_num = []
    for num in temp_num:
        if lefted >= num:
            replace_num.append(num)
            lefted -= num
            result += 1
    temp_num = replace_num
print(result)
