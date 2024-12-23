import re

ret = 0
while True:
    try:
        inp = input()
        nums = re.findall(r'mul\((\d+),(\d+)\)', inp)
        for pair in nums:
            ret += int(pair[0]) * int(pair[1])
    except:
        break
print(ret)
