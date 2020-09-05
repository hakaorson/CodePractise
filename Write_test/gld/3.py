n = int(input())
nums = list(map(int, input().split(' ')))


def sortarray(array):
    n = len(array)
    ls = sorted(array)
    count = 0
    j = n-1
    for i in range(n-1, -1, -1):
        if ls[j] == array[i]:
            count += 1
            j -= 1
    return n-count


print(sortarray(nums))

# n = int(input())
# nums = list(map(int, input().split(' ')))
# max_num = nums[0]
# result = 0
# for num in nums:
#     if num < max_num:
#         result += 1
#     else:
#         max_num = num
# print(result)