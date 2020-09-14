strs = list(input())
result = 0
remmenber = {}
for index, char in enumerate(strs):
    if char in remmenber.keys():
        result = max(result, index-remmenber[char])
    remmenber[char] = index

print(result)
