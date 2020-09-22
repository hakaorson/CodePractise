'''
1
8
6 9 6 3 6 9 6 3
'''
import collections
n = int(input())

for ni in range(n):
    size = int(input())
    result_rec, result_same = 0, 0
    nums = list(map(int, input().split()))
    statics = collections.Counter(nums)
    for i in statics:
        temp_same = statics[i]//4
        result_same += temp_same
        statics[i] -= temp_same*4

        if statics[i] >= 2:
            result_rec += 1
    result_rec = result_rec//2
    print(" ".join(map(str, [result_same, result_rec])))
