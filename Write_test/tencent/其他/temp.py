import collections
import heapq
n, k = list(map(int, input().split()))

words = []
for i in range(n):
    words.append(input())
dic = collections.Counter(words)

heap1, ans1 = [], []
for i in dic:
    heapq.heappush(heap1, (dic[i], i))
for _ in range(k):
    ans1.append(heapq.heappop(heap1))

heap, ans = [], []
for i in dic:
    heapq.heappush(heap, (-dic[i], i))
for _ in range(k):
    ans.append(heapq.heappop(heap))
for item in ans:
    print(" ".join(map(str,item)))
for item in ans1:
    print(" ".join(map(str,item)))
