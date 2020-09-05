'''
n = input()
num_a = list(map(int, input().split()))
'''
n = 4
num_a = [1, 3, 7, 15]
num_b = [num_a[i]-num_a[i-1]for i in range(1, len(num_a))]
for num in num_b:
    if num <= 0:
        print(-1)


def gcd(p, q):
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)


result = num_b[0]
if len(num_b) == 1:
    print(num_b[0])
else:
    for index in range(1, len(num_b)):
        result = gcd(num_b[index], result)
print(result)
