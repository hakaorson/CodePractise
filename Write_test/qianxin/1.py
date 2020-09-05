n = 5
# array = [[0 for j in range(n+1)]for i in range(n+1)]
# # array[i][j]表示数字j分成i坨的分法

# array = [0 for i in range(n+1)]  # array[i]表示数字i分解的所有可能
# array[0] = 1
# for i in range(1, n+1):
#     tempsum = 0
#     for j in range(i):
#         tempsum += array[j]
#     array[i] = tempsum
# pass

n = int(input())
ans = 1
di = 2
mi = n-1
while(mi):
    if(mi & 1):
        ans *= di
    di *= di
    mi >>= 1
print(ans % int(1e9+7))
