# 123 12345678 123abcABC!!!

import re


def check(single_str):
    result = {'0': 0, '*': 0, 'a': 0, 'A': 0}
    result['0'] = len(re.findall('[0-9]', single_str))
    result['a'] = len(re.findall('[a-z]', single_str))
    result['A'] = len(re.findall('[A-Z]', single_str))
    result['*'] = len(single_str)-result['0']-result['a']-result['A']
    if len(single_str) >= 8 and len(single_str) <= 120:
        if result['0'] and result['a'] and result['A'] and result['*']:
            print(0)
        else:
            print(2)
    else:
        print(1)
    pass


strs = list(input().split())
for single_str in strs:
    check(single_str)
