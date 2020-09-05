# # n = 1
# # all_datas = [[4, 3, 1, 2, 5, 6]]
# n = int(input())
# all_datas = []
# for i in range(n):
#     all_datas.append(list(map(int, input().split())))
# result_map = {}


# def getseq(nums_short):
#     result = nums+nums
#     short_index = nums_short.index(min(nums_short))
#     return result[short_index:short_index+4]


# def getcode(nums):
#     first_index = nums.index(1)
#     if first_index % 2 == 0:
#         result = []
#         result.append(nums.pop(first_index))
#         result.append(nums.pop(first_index))
#         nums[1], nums[2] = nums[2], nums[1]
#     else:
#         result = []
#         result.append(nums.pop(first_index))
#         result.append(nums.pop(first_index-1))
#         last = nums.pop(-1)
#         nums.insert(1, last)
#     result.extend(getseq(nums))
#     return result


# for nums in all_datas:
#     temp_seq = tuple(getcode(nums))
#     if temp_seq in result_map.keys():
#         result_map[temp_seq] += 1
#     else:
#         result_map[temp_seq] = 1
# result = []
# for key in result_map.keys():
#     result.append(result_map[key])
# result = sorted(result, reverse=True)
# print(len(result))
# print(' '.join(map(str, result)))
N = int(input())
res = {}
for i in range(N):
    arr = list(map(int, input().split()))
    arr = sum(sorted([sorted(arr[:2]), sorted(arr[2:4]),
                      sorted(arr[4:])], key=lambda x: x[0]), [])
    arr = list(map(str, arr))
    key = "".join(arr)
    res.setdefault(key, 0)
    res[key] += 1
res = sorted(res.values(), reverse=True)
print(len(res))
print(" ".join(map(str, res)))
# for i in range(len(res)-1):
#     print(res[i])
