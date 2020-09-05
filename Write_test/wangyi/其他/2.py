'''
n, D = list(map(int, input().split()))
breaks = list(map(int, input().split()))
damage = list(map(int, input().split()))
'''

n, D = [3, 50]
breaks = [100, 50, 51]
damage = [1000, 1000, 1000]
final_result = sum(damage)


def getresult(left_break, left_damage, now_defence, now_result, final_result):
    if len(left_break) == 0:
        return now_result
    for i in range(len(left_break)):
        temp_break = left_break.pop(i)
        temp_damage = left_damage.pop(i)
        temp_result = temp_damage if now_defence <= temp_break else 0
        final_result = min(final_result, getresult(left_break, left_damage,
                                                   now_defence+1, now_result+temp_result, final_result))
        left_break.insert(i, temp_break)
        left_damage.insert(i, temp_damage)
    return final_result


result = getresult(breaks, damage, D, 0, final_result)

print(final_result)
