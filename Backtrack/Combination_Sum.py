class Solution:
    def combinationSum(self, candidates, target):
        self.all_result = []
        candidates = sorted(candidates, reverse=True)
        self.dfs(candidates, target, [])
        print(self.all_result)

    def dfs(self, candidates, target, current):
        if target == 0:
            sing_ret = current.copy()
            sing_ret.reverse()
            self.all_result.append(sing_ret)
            return
        elif len(candidates) == 0:
            return
        else:
            self.dfs(candidates[1:], target, current)
            candi = candidates[0]
            if candi <= target:
                current.append(candi)
                self.dfs(candidates, target-candi, current)
                current.pop(-1)


solu = Solution()
solu.combinationSum([2, 3, 6, 7], 8)
