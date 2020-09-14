
# strings=input()
import re


def downandup(strinput: str):
    result = strinput.lower()
    result = result[0].upper()+result[1:]
    return result


strings = input()
patten = re.compile('[^0-9a-zA-Z]')

lists = re.split(patten, strings)

finalresult = ''
for item in lists:
    if len(item):
        finalresult += downandup(item)
finalresult = finalresult[0].lower()+finalresult[1:]
print(finalresult)
