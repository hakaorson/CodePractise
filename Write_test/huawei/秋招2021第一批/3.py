string, n = input().split(',')
n = int(n)
result = [[] for _ in range(n)]
cycle = (n-1)*2-1
list1 = [index for index in range(n-1)]
list2 = [index for index in range(n-1, 0, -1) if index != n//2]
listsum = []
for i in range(len(list2)):
    listsum.append(list1[i])
    listsum.append(list2[i])
listsum.append(list1[-1])
for index, char in enumerate(string):
    tempindex = listsum[index % cycle]
    result[tempindex].append(char)

for item in result:
    print(''.join(item), end='')
print('\n')
