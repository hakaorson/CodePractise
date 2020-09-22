'''
2
ABCABDABDABEABEABF
ABCABDAEC
'''


def check(s, size, index):
    target = s[index]
    while index < len(s):
        if s[index] != target:
            return False
        index += 3
    return True


n = int(input())
for i in range(n):
    s = input()
    if len(s) % 3:
        print('False')
    else:
        size = len(s)//3
        res = 0
        res += check(s, size, 0)
        res += check(s, size, 1)
        res += check(s, size, 2)
        if res >= 2:
            print('True')
        else:
            print('False')
