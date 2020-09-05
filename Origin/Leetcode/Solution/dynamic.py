class Solution():
    def minDistance(self, word1, word2):
        '''
        本质，对于两个末尾字符相同的子序列，那么这两个序列的距离就是分别忽略末尾字符后的距离
        对于两个末尾字符不同的子序列，那么要充分考虑分别的倒数第二位字符的匹配目标
        '''
        first_d = len(word1)+1
        second_d = len(word2)+1
        dp = [[0 for j in range(second_d)] for i in range(first_d)]
        for i in range(first_d):
            dp[i][0] = i
        for j in range(second_d):
            dp[0][j] = j
        for i in range(1, first_d):
            for j in range(1, second_d):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j])+1
        return dp[len(word1)][len(word2)]

    def maxProduct(self, nums):
        # 求数组最大连续乘积
        '''
        nums = [1]+nums
        dp_max = [1 for i in range(len(nums))]
        dp_min = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp_max[i] = max(nums[i], dp_max[i-1]*nums[i])
                dp_min[i] = min(nums[i], dp_min[i-1]*nums[i])
            else:
                dp_max[i] = max(nums[i], dp_min[i-1]*nums[i])
                dp_min[i] = min(nums[i], dp_max[i-1]*nums[i])
        return max(dp_max[1:])
        '''
        # 思想：对于不存在0的任意一段，如果需要得到乘积最大值，那么一定需要乘上尽可能多的数（在负数个数为偶数的前提下）
        left_temp = nums[0]
        right_temp = nums[-1]
        result = max(left_temp, right_temp)
        for i in range(1, len(nums)):
            left_temp = nums[i]*(left_temp or 1)
            right_temp = nums[len(nums)-1-i]*(right_temp or 1)
            result = max(result, left_temp, right_temp)
        return result

    def isInterleave(self, s1, s2, s3):
        '''
        # 两个string保持原顺序是否能形成另外一个
        # 深度优先搜索，朴素的思想
        if (len(s1)+len(s2)) != len(s3):
            return False

        def check(s1_temp, s2_temp, s3_temp):
            if len(s3_temp) == 0:
                return True
            else:
                temp_result = False
                if len(s1_temp) > 0 and s1_temp[0] == s3_temp[0]:
                    temp_result = check(s1_temp[1:], s2_temp, s3_temp[1:]) or temp_result
                if len(s2_temp) > 0 and s2_temp[0] == s3_temp[0]:
                    temp_result = check(s1_temp, s2_temp[1:], s3_temp[1:]) or temp_result
                return temp_result
        return check(s1, s2, s3)
        '''
        # 判断任何两段组合能不能形成形成新的组合，如果可以那么（不管他们怎么组合的，只需要判断有没有可能性）
        if len(s3) != len(s1)+len(s2):
            return False
        s1 = '**'+s1
        s2 = '**'+s2
        s3 = '****'+s3  # 去除边界判断
        dp_matrix = [[False for j in range(len(s2))]for i in range(len(s1))]
        for i in range(len(s1)):
            dp_matrix[i][0] = True
        for j in range(len(s2)):
            dp_matrix[0][j] = True
        for i in range(1, len(s1)):
            for j in range(1, len(s2)):
                if (dp_matrix[i-1][j] and s1[i] == s3[i+j+1]) or (dp_matrix[i][j-1] and s2[j] == s3[i+j+1]):
                    dp_matrix[i][j] |= True
        return dp_matrix[len(s1)-1][len(s2)-1]

    def findLength(self, A, B):  # 最长公共子数组
        # 使用二维dp算法，每个位置放置一个数，代表这个对应位置为结束两个数组的最长公共子数组
        # 只有在前面是公共子数组并且接下来两个相同才能加一
        A_bound = ['#']+A
        B_bound = ['#']+B
        dp_matrix = [[0 for j in range(len(B_bound))]for i in range(len(A_bound))]
        result = 0
        for i in range(1, len(A_bound)):
            for j in range(1, len(B_bound)):
                if A_bound[i] == B_bound[j]:
                    dp_matrix[i][j] = dp_matrix[i-1][j-1]+1
                    result = max(result, dp_matrix[i][j])
        return result

    def findTargetSumWays(self, nums, S):
        # 关键是一堆数中寻找特定的组合，形成某一个数的方案数，可以用动态规划的方法，已经得到了前i个数组成目标数的方式，那么考虑第i+1个数可以分成考虑包含第i+1和不包含第i+1两种情况
        '''
        #使用了二维dp，且没有提前终止计算
        nums = [0]+nums  # 去除边界判断，默认最开始是+0
        the_sum = sum(nums)
        if the_sum < S or (S+the_sum) % 2 == 1:
            return 0
        target = (S+the_sum)//2

        dp_matrix = [[0 for j in range(len(nums))]for i in range(target+1)]
        dp_matrix[0][0] = 1  # 初始化
        for j in range(1, len(nums)):
            for i in range(0, target+1):
                if i-nums[j] >= 0:
                    dp_matrix[i][j] = dp_matrix[i][j-1]+dp_matrix[i-nums[j]][j-1]
                else:
                    dp_matrix[i][j] = dp_matrix[i][j-1]
        return dp_matrix[target][len(nums)-1]
        '''
        nums = [0]+nums  # 去除边界判断，默认最开始是+0
        the_sum = sum(nums)
        if the_sum < S or (S+the_sum) % 2 == 1:
            return 0
        target = (S+the_sum)//2

        dp_array = [0 for i in range(target+1)]
        dp_array[0] = 1
        for j in range(1, len(nums)-1):  # len(nums)-1避免最后一轮计算全部
            for i in range(target, nums[j]-1, -1):
                # range总是靠左，这里相当于(0,target+1)取反
                # 之所以从大到小，因为大的计算F需要使用到小的那部分数值，因此计算大的之后对小的计算不产生影响
                dp_array[i] += dp_array[i-nums[j]]
        return dp_array[target]+(dp_array[target-nums[-1]] if target-nums[-1] >= 0 else 0)
        '''
        # 参考代码
        if sum(nums) < S or (sum(nums)+S) % 2 == 1:
            return 0
        P = (sum(nums)+S)//2
        dp = [1] + [0 for _ in range(P)]
        for i in range(len(nums)):
            for j in range(P, nums[i]-1, -1):  # 这个nums[i]-1是关键，如果和比当前的数还小，那么就没有包含当前数的情况
                dp[j] = dp[j]+dp[j-nums[i]]
        return dp[-1]
        '''

    def longestPalindrome(self, s):
        # 最长回文子串，使用动态规划的方法，如果一个串是回文串，那么这个穿一定是在回文串的基础上两端添加了相同的符号
        dp_matrix = [[True for j in range(len(s))]for i in range(len(s))]
        result_left, result_right = 0, 0
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and dp_matrix[i+1][j-1]:
                    if j-i > result_right-result_left:
                        result_left, result_right = i, j
                else:
                    dp_matrix[i][j] = False
        return s[result_left:result_right+1]

    def maximalSquare(self, matrix):
        '''
        # 二维7数组中寻找最大正方形
        if not(len(matrix)):
            return 0
        matrix = [list(map(int, row)) for row in matrix]

        def has_one(temp_matrix):
            for row in temp_matrix:
                for num in row:
                    if num:
                        return True
            return False

        def check(temp_matrix, depth):
            row_size = len(temp_matrix)-1
            col_size = len(temp_matrix[0])-1
            for i in range(0, row_size):
                for j in range(0, col_size):
                    if temp_matrix[i][j] and temp_matrix[i+1][j] and temp_matrix[i][j+1]and temp_matrix[i+1][j+1]:
                        temp_matrix[i][j] = 1
                    else:
                        temp_matrix[i][j] = 0
            left_matrix = [[matrix[i][j] for j in range(col_size)] for i in range(row_size)]  # 注意list不能直接切片
            return left_matrix, depth+1
        depth = 0
        while has_one(matrix):
            matrix, depth = check(matrix, depth)
        return depth*depth
        '''
        # 使用动态规划的方法
        result = 0
        if len(matrix) == 0:
            return result
        dp_shape = [len(matrix)+1, len(matrix[0])+1]
        dp_matrix = [[0 for j in range(dp_shape[1])] for i in range(dp_shape[0])]
        for i in range(1, dp_shape[0]):
            for j in range(1, dp_shape[1]):
                refer_size = min(dp_matrix[i-1][j], dp_matrix[i][j-1])
                if matrix[i-refer_size-1][j-refer_size-1] == '1' and matrix[i-1][j-1] == '1':
                    dp_matrix[i][j] = refer_size+1
                    result = max(result, dp_matrix[i][j])
                elif matrix[i-1][j-1] == '1':
                    dp_matrix[i][j] = refer_size
        return result*result

    def maximalRectangle(self, matrix):
        # 二维数组中寻找最大矩形
        result = 0
        if len(matrix) == 0:
            return result
        dp_shape = [len(matrix)+1, len(matrix[0])+1]
        dp_matrix = [[[0, 0] for j in range(dp_shape[1])] for i in range(dp_shape[0])]
        for i in range(1, dp_shape[0]):
            for j in range(1, dp_shape[1]):
                if matrix[i-1][j-1] == '1':
                    left_size_x, left_size_y = dp_matrix[i][j-1]
                    upper_size_x, upper_size_y = dp_matrix[i-1][j]
                    if True:
                        test_pos_x, test_pos_y = i-upper_size_x, j-left_size_y
                        test_size_x, test_size_y = dp_matrix[test_pos_x][test_pos_y]
                        result_x, result_y = test_size_x+upper_size_x, test_size_y+left_size_y
                        dp_matrix[i][j] = [result_x, result_y]
                        result = max(result, result_x*result_y)
        return result

    def longestCommonSubsequence(self, text1, text2):
        # 寻找两个字符串的最长公共子串，注意这个公共子串可以是不连续的
        # 关键是考虑当前比对的两个符号对前面有什么影响
        '''
        dp_matrix = [[0 for j in range(len(text2)+1)]for i in range(len(text1)+1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp_matrix[i+1][j+1] = dp_matrix[i][j]+1
                else:
                    dp_matrix[i+1][j+1] = max(dp_matrix[i][j+1], dp_matrix[i+1][j])
        return dp_matrix[-1][-1]
        '''
        dp_list = [0 for _ in range(len(text2)+1)]
        for i in range(len(text1)):
            dp_list_temp = [0 for _ in range(len(text2)+1)]
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp_list_temp[j+1] = dp_list[j]+1
                else:
                    dp_list_temp[j+1] = max(dp_list_temp[j], dp_list[j+1])  # 关键是前面计算会覆盖一定的数据，被覆盖的数据会对后面的数据产生影响
            dp_list = dp_list_temp
        return dp_list[-1]

    def maxProfit(self, k, prices):
        if k > prices//2:
            k = prices//2
        prices = [0]+prices  # 经过操作选择后的状态
        k = k+1  # 当前处于第i次交易中，是一个左闭右开的区间
        dp_maxtrix = [[[0, -max(prices)]for trade in range(k)] for day in range(len(prices))]  # 其中每一个状态都表示在这个状态下的盈利
        for day in range(1, len(prices)):
            for trade in range(1, k):
                dp_maxtrix[day][trade][0] = max(dp_maxtrix[day-1][trade][0], dp_maxtrix[day-1][trade][1]+prices[day])
                dp_maxtrix[day][trade][1] = max(dp_maxtrix[day-1][trade][1], dp_maxtrix[day-1][trade-1][0]-prices[day])
        return dp_maxtrix[-1][-1][0]


if __name__ == '__main__':
    solu = Solution()
    # result = solu.findTargetSumWays([1, 1, 10, 10, 1], 3)
    # result = solu.longestPalindrome('12343557')
    matrix = [["1", "0", "0", "1"], ["1", "1", "0", "1"], ["1", "1", "1", "1"], ["0", "1", "1", "1"], ["0", "1", "1", "1"]]
    # result = solu.maximalSquare(matrix)
    # result = solu.maximalRectangle(matrix)
    # result = solu.longestCommonSubsequence("g", "gg")
    # result = solu.longestCommonSubsequence("pmjghexybyrgzczy", "hafcdqbgncrcbihkd")
    result = solu.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4])
    pass
