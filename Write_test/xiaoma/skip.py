colors = [1, 2, 4, 1, 4, 2]
curs = {}
sits = []
for index, color in enumerate(colors[::-1]):
    if color in curs.keys():
        sits.append(curs[color])
    else:
        sits.append(-1)
    curs[color] = len(colors)-index-1
sits = list(reversed(sits))
dyna = [len(colors)for _ in range(len(colors))]
dyna[-1] = 0
for index in range(len(colors)-1):
    temp_index = len(colors)-index-2
    if sits[temp_index] == -1:
        dyna[temp_index] = dyna[temp_index+1]+1
    else:
        dyna[temp_index] = min(dyna[temp_index+1]+1, dyna[sits[temp_index]]+1)
    pass
print(dyna[0])
