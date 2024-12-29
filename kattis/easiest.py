def get_digits(a: int) -> list[int]:
    ret: list[int] = list()
    if a == 0:
        ret.append(0)
    while a != 0:
        ret.append(a % 10)
        a //= 10
    return ret
while True:
    if (a:=int(input())) == 0: break
    else:
        target_sum = sum(get_digits(a))
        ret = 11
        while sum(get_digits(ret * a)) != target_sum:
            ret += 1
        print(ret)
