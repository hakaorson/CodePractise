PARA='paradox'
K_num, N_num = list(map(int, input().split()))
array = list(map(int, input().split()))
back_count = 0
if K_num == 0:
    print(PARA)
for i in range(N_num):
    if array[i] == K_num:
        K_num -= array[i]
        print(PARA)
        break
    elif array[i] < K_num:
        K_num -= array[i]
    else:
        K_num = array[i]-K_num
        back_count += 1
if K_num > 0:
    print(K_num, back_count)
