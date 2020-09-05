def backPack_dynamic_n_m(m, A):
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


n = int(input())
nums = list(map(int, input().split()))
target = int(input())
if n == 0:
    print(1)
elif target == 0:
    print(0)
else:
    cut = sum(nums)//2
    if sum(nums) % 2 == 1:
        cut += 1
    result = backPack_dynamic_n_m(cut, nums)
    minest = max(result, sum(nums)-result)
    if target >= minest:
        print(1)
    else:
        print(0)
