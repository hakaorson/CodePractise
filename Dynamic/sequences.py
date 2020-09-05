nums = [2, 7, 1, 5, 6, 4, 3, 8, 9]
length = len(nums)
pres = [-1 for i in range(length)]
max_lenght = [1 for i in range(length)]
for i in range(length):
    max_index = -1
    for k in range(0, i):
        if nums[k] < nums[i]:
            if max_index == -1:
                max_index = k
            elif max_lenght[k] > max_lenght[max_index]:
                max_index = k
    pres[i] = max_index
    if max_index != -1:
        max_lenght[i] = max_lenght[max_index]+1
result_index = max_lenght.index(max(max_lenght))
result = []
while result_index != -1:
    result.insert(0, result_index)
    result_index = pres[result_index]
for ind in result:
    print(nums[ind])