class Solution:
    def canPartition(self, nums) -> bool:
        target = sum(nums)
        if target % 2:
            return False
        target = target//2
        matrix = [[0 for j in range(len(nums)+1)]for i in range(target+1)]
        for i in range(1, target+1):
            for j in range(1, len(nums)+1):
                if i-nums[j-1] >= 0:
                    value_take = matrix[i-nums[j-1]][j-1]+nums[j-1]
                else:
                    value_take = 0
                value_no_take = matrix[i][j-1]
                matrix[i][j] = max(value_take, value_no_take)
        if matrix[-1][-1] == target:
            return True
        else:
            return False


solu = Solution()
solu.canPartition([1, 5, 11, 5])
