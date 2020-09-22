nums = [1, 1]
target = int(input())
if target <= 0:
    pass
else:
    if target > 2:
        for i in range(2, target):
            nums.append(nums[-1]+nums[-2])
    temp = []
    for i in range(1, target+1):
        temp.append(nums[i-1])
        for j in temp:
            print(j, " ", end="")
        for j in range(len(temp)-1):
            print(nums[i-j-2], " ", end="")
        print()
        # for j in range(i-1):
        #     temp.append(nums[j])
        # temp.append(nums[i-1])
        # for j in range(i-1):
        #     temp.append(nums[i-1-j-1])
        # print(" ".join(map(str, temp)))
