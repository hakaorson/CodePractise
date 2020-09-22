class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        ans = set()

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):  # 固定两个数
                left = j+1  # 左指针
                right = len(nums)-1  # 右指针
                while(right > left):
                    temp = nums[i]+nums[j]+nums[left]+nums[right]
                    if temp == target:
                        ans.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    if temp > target:
                        right -= 1
                    if temp < target:
                        left += 1
        return list(ans)
