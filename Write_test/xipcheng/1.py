def divingBoard(a, b, k):
    if k == 0:
        return []
    min_num = min(a, b)
    max_num = max(a, b)
    base = k*min_num
    result = []
    for i in range(k):
        result.append(base+i*(max_num-min_num))
    result.append(k*max_num)
    # print(str(result))
    return result


divingBoard(1, 2, 0)
