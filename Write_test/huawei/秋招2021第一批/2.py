nums = [5, 5, 5, 10]
coin5 = 0
coin10 = 0
for i in nums:
    if i == 5:
        coin5 += 1
    elif i == 10:
        if !coin5:
            print('false')
        else:
            coin5 -= 1
            coin10 += 1
    else:
        if (coin5 and coin10)or coin5>=3:
            coi
