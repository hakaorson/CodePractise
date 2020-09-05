'''
Leetcode 10

给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
'''


class Solution_dynamic():
    def isMatch(self, s, p):
        s, p = '%#'+s, '%#'+p
        matrix = [[False for j in range(len(p))]for i in range(len(s))]
        matrix[0][0] = True
        for i in range(1, len(s)):
            for j in range(1, len(p)):
                if s[i] == p[j] or p[j] == '.':
                    matrix[i][j] = matrix[i-1][j-1]
                elif p[j] == '*':
                    if s[i] == p[j-1] or p[j-1] == '.':
                        # 关键要注意时刻保持选择的权力
                        matrix[i][j] = matrix[i-1][j] or matrix[i][j-2]
                    else:
                        matrix[i][j] = matrix[i][j-2]
                else:
                    matrix[i][j] = False
        return matrix[-1][-1]


class Solution_recursive():
    def isMatch(self, s, p):
        if s == '' and p == '':
            return True
        elif p == '':
            return False
        else:
            if len(p) >= 2 and p[1] == '*':  # 主要考虑*的情况
                if s and (s[0] == p[0] or p[0] == '.'):
                    return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
                    '''
                    一种情况是考虑现在匹配一个，其他什么都不变
                    还尊一种情况是考虑现在匹配了零个，其他什么都不变
                    '''
                else:
                    return self.isMatch(s, p[2:])  # 这种情况只能匹配零个
            else:
                if s and (s[0] == p[0] or p[0] == '.'):
                    return self.isMatch(s[1:], p[1:])
                else:
                    return False


s = 'ab'
p = '.*'
'''
solu_recursive = Solution_recursive()
result_recursive = solu_recursive.isMatch(s, p)
print(result_recursive)
'''
solu_dynamic = Solution_dynamic()
result_dynamic = solu_dynamic.isMatch(s, p)
print(result_dynamic)
