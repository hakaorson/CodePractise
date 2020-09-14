class Solution:
    def numberofprize(self, a, b, c):
        self.lists = [a, b, c]
        self.sum = sum(self.lists)
        minest = min(self.lists)
        maxest = max(self.lists)
        result = self.getresult(minest, maxest)
        return result

    def check(self, target):
        biggersum = 0
        littlersum = 0
        for i in self.lists:
            if i > target:
                biggersum += i-target
            else:
                littlersum += target-i
        if biggersum//2 >= littlersum:
            return True
        else:
            return False

    def getresult(self, minnum, maxnum):
        if minnum != maxnum:
            #题目要求倾向于找偏大的值
            middle = (minnum+maxnum)//2 if ((minnum+maxnum) %
                                            2 == 0) else (minnum+maxnum)//2+1
            if self.check(middle):
                return self.getresult(middle, maxnum)
            else:
                return self.getresult(minnum, middle-1)
        else:
            return minnum


solu = Solution()
solu.numberofprize(8, 3, 3)
