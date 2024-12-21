from typing import Sequence
reports: list[list[int]] = list()
def is_decreasing(s: Sequence[int], start: int, end: int) -> bool:
    if end - start <= 0: return True
    return (first := s[start]) > (second := s[start + 1]) and first - second <= 3 and is_decreasing(s, start + 1, end)
def is_increasing(s: Sequence[int], start: int, end: int) -> bool:
    if end - start <= 0: return True
    return (first := s[start]) < (second := s[start + 1]) and second - first <= 3 and is_increasing(s, start + 1, end)

if __name__ == "__main__":
    ret = 0
    while True:
        try:
            report = list(map(int, input().split()))
            l = len(report)
            if is_increasing(report, 0, l -1) or is_decreasing(report, 0, l -1):
                ret += 1
        except:
            break
    print(ret)
