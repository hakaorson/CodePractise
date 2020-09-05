N, M, T = list(map(int, input().split()))
middle = []
dinner = []
for i in range(N):
    middle.append(tuple(map(int, input().split())))
for i in range(M):
    dinner.append(tuple(map(int, input().split())))


def single(Nums):
    result = Nums[-1][0]
    index = len(Nums)-1
    while index >= 0 and Nums[index][1] >= T:
        result = min(result, Nums[index][0])
    print(result)


def double(Nums0, Nums1):
    result = Nums0[-1][0]+Nums1[-1][0]
    for num0 in Nums0:
        for num1 in Nums1:
            if num0[1]+num1[1] >= T:
                result = min(result, num0[0]+num1[0])
    print(result)

    # Nums0.insert(0, (0, 0))
    # Nums1.insert(0, (0, 0))

    # current = Nums0[-1][1]+Nums1[-1][1]
    # result = Nums0[-1][0]+Nums1[-1][0]
    # index0 = len(Nums0)-1
    # index1 = len(Nums1)-1
    # while index0 and index1 and current >= T:

    # while
    # pass


if T == 0:
    print(0)
middle = sorted(middle, key=lambda x: x[1])
dinner = sorted(dinner, key=lambda x: x[1])
if middle and dinner:
    if middle[-1][1]+dinner[-1][1] < T:
        print(-1)
    double(middle, dinner)
elif middle:
    if middle[-1][1] < T:
        print(-1)
    single(middle)
elif dinner:
    if dinner[-1][1] < T:
        print(-1)
    single(dinner)
else:
    print(-1)
