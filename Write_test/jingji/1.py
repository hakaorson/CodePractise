import collections


class Solution:
    def minOps(self, Y, X):
        xcol = collections.Counter(X)
        ycol = collections.Counter(Y)
        if xcol != ycol:
            return -1
        ycur = len(Y)
        result = 0
        for i in range(len(X)-1, -1, -1):
            ycur -= 1
            target = X[i]
            ypre = ycur
            while ycur >= 0 and Y[ycur] != target:
                ycur -= 1
            result += (ypre-ycur)
            if ycur == -1:
                break
        return result


Solution().minOps("AABAA","AAABA")
