n, m = 2, 3
n, m = list(map(int, input().split()))
result = pow(n, m)-n*pow(n-1, m-1)
result = result % 100003
print(result)

result = pow(n, m) % 100003-(n*pow(n-1, m-1)) % 100003
print(result)
