nums = list(map(int, input()))

# nums = [9, 9, 8, 8, 7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1, 1]
nums.append(9)
curmin = 9
curminindex = len(nums)-1
situation = [-1 for i in range(10)]
success = False
for index in range(len(nums)-2, -1, -1):
    for cantidate in range(nums[index]-1, -1, -1):
        if situation[cantidate] != -1:
            nums[index], nums[situation[cantidate]
                              ] = nums[situation[cantidate]], nums[index]
            success = True
            break
    if success is True:
        break
    situation[nums[index]] = index
if curminindex == 0 or nums[0] == 0 or success is False:
    print(0)
else:
    result = ''.join(map(str, nums[:len(nums)-1]))
    print(result)
