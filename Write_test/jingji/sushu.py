class Solution:
    def countPrimes(self, n):
        # write code here
        nums = [True for i in range(n+1)]
        beginnum = 2
        while(beginnum <= n):
            if nums[beginnum] is True:
                cur = beginnum*beginnum
                while(cur <= n):
                    nums[cur] = False
                    cur += beginnum
                beginnum += 1
            else:
                beginnum += 1
        nums.pop(-1)
        return sum(nums[2:])


# solu = Solution()
# solu.countPrimes(11)
