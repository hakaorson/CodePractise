numsxy = list(map(int, input().split()))
numsyx = list(map(int, input().split()))
if len(numsyx) <= 1 or len(numsxy) == 0:
    print(-1)
else:
    minxy = [0 for i in range(len(numsxy))]
    minxy[0] = numsxy[0]
    minyx = [0 for i in range(len(numsyx))]
    minyx[-1] = numsyx[-1]
    for i in range(1, len(numsxy)):
        minxy[i] = min(minxy[i-1], numsxy[i])
    for i in range(len(numsyx)-2, -1, -1):
        minyx[i] = min(minyx[i+1], numsyx[i])
    candidate = min(len(numsxy), len(numsyx)-1)
    result = numsxy[0]+numsyx[1]
    for i in range(candidate):
        result = min(minxy[i]+minyx[i+1], result)
    print(result)
