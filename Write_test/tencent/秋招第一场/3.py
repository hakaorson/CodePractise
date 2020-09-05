n = int(input())


def nums2int(nums):
    nums = list(map(int, list(str(nums))))
    return sum(nums)


for i in range(n):
    t = int(input())
    result = 0
    for i in range(1, t//2+1):
        nums1 = i
        nums2 = t-i
        result = max(result, nums2int(nums1)+nums2int(nums2))
    print(result)
