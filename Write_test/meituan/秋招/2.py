n = int(input())
trips = {}
for i in range(n):
    v0, v1 = list(input().split())
    if v0 in trips.keys():
        trips[v0].append(v1)
    else:
        trips[v0] = [v1]

for key,vals in trips:
    for val in vals:
        
print(1)
pass
'''
6
b n
n g
g s
s b
f b
b f
'''
