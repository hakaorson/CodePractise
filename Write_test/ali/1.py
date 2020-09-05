n = int(input())
nums1 = list(map(int, list(input())))
nums2 = list(map(int, list(input())))


def check(nums1, nums2):
    cur1_0 = 0
    cur0_1 = 0
    cur_exchange = 0
    for i in range(n):
        if nums1[i] == nums2[i]:
            pass
        elif nums2[i] == 1:
            if cur1_0:
                cur1_0 -= 1
                cur_exchange += 1
            else:
                cur0_1 += 1
        else:
            if cur0_1:
                cur0_1 -= 1
                cur_exchange += 1
            else:
                cur1_0 += 1
    return cur0_1+cur1_0+cur_exchange


result1 = check(nums1, nums2)
result2 = check(nums1, list(reversed(nums2)))+1
print(min(result1, result2))
