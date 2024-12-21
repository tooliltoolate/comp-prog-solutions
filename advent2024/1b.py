from collections import Counter
left = list()
right = list()
while True:
    try:
        temp = input().split()
        left.append(temp[0])
        right.append(temp[1])
    except:
        break
num_right = Counter(right)
print(sum(map(lambda x: int(x) * num_right[x], left)))
