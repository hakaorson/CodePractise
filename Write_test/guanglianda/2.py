nums = [9, 44, 16, 16, 15, 3, 5, 5, 5, 100, 15, 15, 10, 7]
sums = sum(nums)
lenght = len(nums)
nums.sort(reverse=True)
target = nums[0]
while target >= 0:
    temp = 0
    for num in nums:
        jian = num-target
        if jian > 0:
            if jian % 2 == 1:
                temp += (jian+1)//2
                temp -= 1
            else:
                temp += jian//2
        else:
            temp += jian
    if temp != 0:
        if temp > 0:
            print(-1)
            break
        else:
            target -= max(1, temp//lenght)
    else:
        break
if target == -1:
    print(-1)
else:
    print(target*lenght)
