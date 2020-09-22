'''
3
4
1 2 3 4
4
2 1 4 3
4
3 2 2 4
'''
n = int(input())

for ni in range(n):
    size = int(input())
    nums = list(map(int, input().split()))
    cur_odd, cur_even = 0, 0
    res = 0
    for index, num in enumerate(nums):
        if (index+1) % 2 != num % 2:
            if (index+1) % 2:
                if cur_even:
                    cur_even -= 1
                    res += 1
                else:
                    cur_odd += 1
            else:
                if cur_odd:
                    cur_odd -= 1
                    res += 1
                else:
                    cur_even += 1
    if cur_odd or cur_even:
        print(-1)
    else:
        print(res)
