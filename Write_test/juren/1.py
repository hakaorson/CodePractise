# coding=utf-8
import sys
#str = input()
# print(str)

nums = [4, 2, 2, 1, 1, 3]
size = len(nums)
curchoose = [0 for i in range(len(nums))]
# nums = [0]+nums
# target = 5
# matrix = [[0 for j in range(len(nums))] for i in range(target+1)]
# for j in range(len(nums)):
#     matrix[0][j]=1

# for j in range(1, len(nums)):
#     for i in range(1, target+1):
#         tempsum = 0
#         for k in range(min(i, nums[j])+1):
#             if i>=k:
#                 tempsum += matrix[i-k][j-1]
#         matrix[i][j] = tempsum
# print(matrix[-1][-1])
res = 0
listres = []


def dfs(nums, curchoose, target):
    global res
    global listres
    if target < 0 or len(nums) == 0:
        return
    if target == 0:
        res += 1
        listres.append(curchoose.copy())
        return
    num = nums[0]
    nums = nums[1:]
    for j in range(num+1):
        curchoose[size-len(nums)-1] = j
        dfs(nums, curchoose, target-j)
        curchoose[size-len(nums)-1] = 0
    nums = [num]+nums


dfs(nums, curchoose, 5)
print(res)

print('Hello,World!')
