class Solution:
    def minJump(self, jump):
        result = [len(jump) for _ in range(len(jump))]
        result[-1] = 1
        for index in range(len(result)-2, -1, -1):  # 没加入一个元素，当前所有元素更新为最有选择
            if jump[index]+index >= len(jump):
                result[index] = 1
            else:
                result[index] = result[jump[index]+index]+1
            cur = index+1
            while result[cur] > result[index]:
                result[cur] = result[index]+1
                cur += 1
        return(result[0])
        # result[-1] = 0
        # queue = [len(jump)-1]
        # while queue:
        #     temp = queue.pop(0)
        #     for index, num in enumerate(jump[0:temp]):
        #         if temp-index >= num:
        #             queue.append(index)
        #             if result[0:index]:
        #                 result[index] = min(
        #                     min(result[0:index])+1, result[temp]+1)
        #             else:
        #                 result[index] = result[temp]+1
        # return(result[0])


solu = Solution()
solu.minJump([3,7,8,1,2,8,5,9,8,3,2,7,5,1,1])

# jump = [2, 3, 1, 1, 2, 1, 0]
