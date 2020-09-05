'''
去除尽量少的数，使得剩下的数最大值最小值之差小于某一个值
'''
n = 5
x = 2
num = [2, 1, 3, 2, 5]
n, x = list(map(int, input().split()))
num = list(map(int, input().split()))


num = sorted(num)
i = 0
j = 0
max_len = 0
for j in range(1, len(num)):
    right_num = num[j]
    left_num = num[i]
    expand = right_num-left_num
    if expand > x:
        atleast_move = expand-x
        temp_add = 0
        while temp_add < atleast_move:
            temp_add += num[i+1]-num[i]
            i += 1
    j += 1
    max_len = max(max_len, (j-i))
result = len(num)-max_len
print(result)

pass
