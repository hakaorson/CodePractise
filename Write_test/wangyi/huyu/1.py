# nums = list(map(int, input().split()))
# cars = sorted(nums, key=lambda x: x[0], reverse=True)

# " ".join(map(str,nums))
boxNum, personNum = list(map(int, input().split()))
boxNum += 1
boxValueList = list(map(int, input().split()))
boxValueList.insert(0, 0)
boxStatusList = [[]for i in range(boxNum)]
for per in range(personNum):
    actionNum = int(input())
    personnalPrice = 0
    leftHand = 0
    rightHand = 0
    bag = []
    for actIndex in range(actionNum):
        act = list(input().split())
        if act[1] == 'keep':
            if act[0] == 'left':
                bag.append(str(leftHand))
                leftHand = 0
            else:
                bag.append(str(rightHand))
                rightHand = 0
        elif act[1] == 'take':
            target = int(act[2])
            takeResult = target
            if len(boxStatusList[target]):
                takeResult = boxStatusList[target].pop(-1)
            if act[0] == 'left':
                leftHand = takeResult
            else:
                rightHand = takeResult
        else:
            if act[0] == 'left':
                boxStatusList[int(act[2])].append(leftHand)
                leftHand = 0
            else:
                boxStatusList[int(act[2])].append(rightHand)
                rightHand = 0
    for item in bag:
        personnalPrice += boxValueList[int(item)]
    print(personnalPrice)
