'''
10
2 3 4
5 3 2 6
'''
target = int(input())
l, t, n = list(map(int, input().split()))
danges = list(map(int, input().split()))
dangeslist = list([0 for i in range(target+1)])
# for dange in danges:
#     dangeslist[dange] = 1
# dplist = list([-1 for i in range(target+1)])
# dplist[0] = 0
# for i in range(1, target+1):
#     minest = len(danges)
#     for choose in range(l, t+1):
#         startposition = i-choose
#         if startposition < 0:
#             pass
#         elif startposition == 0:
#             minest = min(minest, dangeslist[i])
#         else:
#             if dplist[startposition] != -1:
#                 minest = min(minest, dangeslist[i]+dplist[startposition])
#     dplist[i] = minest
# print(dplist[-1])
print(0)
pass
