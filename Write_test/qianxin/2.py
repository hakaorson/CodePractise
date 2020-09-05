person = [1,3,2,2,1]

# 有序数组，规定相邻数字大小关系的数组
# 135 分发糖果
person.insert(0, 0)
result = [0 for i in range(len(person))]
for i in range(1, len(person)):
    if person[i] > person[i-1]:
        result[i] = result[i-1]+1
    elif i+1 == len(person) or person[i] <= person[i+1] or person[i]==person[i-1]:
        temp = i
        cur = 1
        while(result[temp] == 0):
            result[temp] = cur
            cur += 1
            temp -= 1
        if result[temp+1] >= result[temp] and person[i] != person[i-1]:
            result[temp] = result[temp+1]+1
print(sum(result))
