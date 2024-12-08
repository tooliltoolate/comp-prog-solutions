from functools import reduce
def solve(n: int) -> int:

    #search all nums that are within a digit of it ig?
    #make a function that generates it for a certain n
    def all_nums(m: int) -> list[int]:

        def numberafy(digits: list[int]) -> int:
            return reduce(lambda x, y: x*10 + y, digits)

        if m == 0: return []
        if m == 1: return list(range(10))

        ret: list[int] = list()
        buffa: list[int] = list()

        def recur(last: int, counter: int):
            #current position is keypad[last]
            nonlocal buffa
            if counter == m:
                ret.append(numberafy(buffa))
                return
            #we can either go down or right or repeat
            #we repeat
            buffa.append(last)
            recur(last, counter + 1)
            buffa.pop()
            #if not 0, we can move
            if last != 0:
                for num in (x for x in range(1,10) if (x - 1) // 3 >= (last - 1) // 3 and (x - 1) % 3 >= (last - 1) % 3):
                    buffa.append(num)
                    recur(num, counter + 1)
                    buffa.pop()
                buffa.append(0)
                recur(0, counter + 1)
                buffa.pop()

        for starter in range(1, 10):
            recur(starter, 0)

        return ret

    smallest: int | None = None

    for num in all_nums(1) + all_nums(2) + all_nums(3):
        if smallest == None: smallest = num
        else: smallest = smallest if abs(smallest - n) < abs(num - n) else num

    return smallest if smallest else 0

assert (ans := solve(180)) == 180
assert (ans := solve(83)) == 80 or ans == 86
assert (ans := solve(132)) == 133 or ans == 131
#n = int(input())
#for _ in range(n):
#    print(solve(int(input())))
