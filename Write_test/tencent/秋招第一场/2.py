strings = input()
k = int(input())
allsubstrings = set()
for i in range(len(strings)):
    for j in range(i+1, len(strings)+1):
        allsubstrings.add(strings[i:j])
allsubstrings = list(allsubstrings)
allsubstrings = sorted(allsubstrings)
print(allsubstrings[k-1])
