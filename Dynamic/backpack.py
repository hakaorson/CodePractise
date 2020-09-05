'''
Lintcode https://www.lintcode.com/problem/?tag=backpack

一系列的背包问题
'''


class Solution():

    def backPack_recursive(self, m, A):
        # 重量等于价值的背包问题，相当于背包装满问题
        if m == 0 or len(A) == 0:
            return 0
        stuff = A[0]
        if stuff < m:
            return max(self.backPack(m-A[0], A[1:])+A[0], self.backPack(m, A[1:]))
        else:
            return self.backPack(m, A[1:])

    def backPack_dynamic_n_m(self, m, A):
        A.insert(0, 0)
        matrix = [[0 for j in range(m+1)] for i in range(len(A))]
        for i in range(1, len(A)):
            for j in range(1, m+1):
                with_stuff = matrix[i-1][j-A[i]] + \
                    A[i] if (j-A[i]) >= 0 else 0
                without_stuff = matrix[i-1][j]
                matrix[i][j] = max(with_stuff, without_stuff)
                if matrix[i][j] == m:
                    return m
        return matrix[-1][-1]

    def backPack_dynamic_m(self, m, A):
        A.insert(0, 0)
        matrix = [0 for i in range(m+1)]
        for i in range(1, len(A)):
            for j in range(m, 0, -1):  # 动态规划的时候会受到前面的影响，这样需要从后往前面遍历
                if j >= A[i]:
                    matrix[j] = max(matrix[j], matrix[j-A[i]]+A[i])
                    if matrix[j] == m:  # 可以提前返回
                        return m
        return matrix[-1]

    def backPackII(self, m, A, V):
        # 最普通的01背包问题
        A.insert(0, 0)
        V.insert(0, 0)
        matrix = [[0 for j in range(m+1)] for i in range(len(A))]
        for i in range(1, len(A)):
            for j in range(1, m+1):
                with_stuff = matrix[i-1][j-A[i]]+V[i] if (j-A[i]) >= 0 else 0
                without_stuff = matrix[i-1][j]
                matrix[i][j] = max(with_stuff, without_stuff)
        return matrix[-1][-1]

    def backPackIV(self, nums, target):
        pass


solu = Solution()
'''
result1 = solu.backPack_dynamic_m(10, [3, 4, 8, 5])
result2 = solu.backPackII(10, [2, 3, 5, 7], [1, 5, 2, 4])
'''
result4 = solu.backPackIV([2, 3, 6, 7], 7)
pass
