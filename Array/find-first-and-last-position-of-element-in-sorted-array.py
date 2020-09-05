import sys
'''
Leetcode 34

在排序数组中查找元素的第一个和最后一个位置
'''


class Solution():
    def searchRange(self, nums, target):
        # 排序数组定位某一个元素的边界，采用二分查找
        # 首先明确问题的定义，找到大于目标结点的最小index，找到小于目标结点得最大index，注意如果直接找相等的边界不好定义
        # 明确定义后需要处理边界条件
        nums = [-sys.maxsize-1]+nums+[sys.maxsize]

        def find_right(left, right):  # 在范围内返回大于target的最小idnex
            if left == right:
                return left
            mid = (left+right)//2
            if nums[mid] <= target:
                return find_right(mid+1, right)
            else:
                return find_right(left, mid)

        def find_left(left, right):
            if left == right:
                return left
            mid = (left+right+1)//2  # 注意此时取上整
            if nums[mid] >= target:
                return find_left(left, mid-1)
            else:
                return find_left(mid, right)

        right_index = find_right(0, len(nums)-1)
        left_index = find_left(0, len(nums)-1)
        return [left_index, right_index-2] if right_index-left_index > 1 else [-1, -1]
