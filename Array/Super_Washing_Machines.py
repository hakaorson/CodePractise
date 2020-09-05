class Solution:
    def findMinMoves(self, machines):
        thesum = sum(machines)
        if thesum % len(machines):
            return(-1)
        target = thesum//len(machines)
        result, fluent = 0, 0
        for mac in machines:
            cur_fluent = fluent+mac-target
            result = max(result, cur_fluent-fluent, abs(cur_fluent))
            fluent = cur_fluent
        return result


solu = Solution()
solu.findMinMoves([0, 3, 0])
