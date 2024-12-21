left = list()
right = list()
while True:
    try:
        temp = input().split()
        left.append(temp[0])
        right.append(temp[1])
    except:
        break

left.sort()
right.sort()
print(sum(map(lambda x: abs(int(x[0]) - int(x[1])), zip(left, right))))
