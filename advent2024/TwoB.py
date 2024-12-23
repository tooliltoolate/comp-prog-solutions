from typing import Sequence
reports: list[list[int]] = list()
def is_decreasing(s: Sequence[int], start: int, end: int) -> bool:
    if end - start <= 0: return True
    return (first := s[start]) > (second := s[start + 1]) and first - second <= 3 and is_decreasing(s, start + 1, end)
def is_increasing(s: Sequence[int], start: int, end: int) -> bool:
    if end - start <= 0: return True
    return (first := s[start]) < (second := s[start + 1]) and second - first <= 3 and is_increasing(s, start + 1, end)
def is_safe(s: Sequence[int]) -> bool:
    l = len(s)
    return is_increasing(s, 0, l - 1) or is_decreasing(s, 0, l - 1)
def without_idx(s: Sequence[int], idx: int) -> list[int]:
    return list(s[:idx]) + list(s[idx + 1:])
def still_safe(s: Sequence) -> bool:
    if is_safe(s): return True
    else: return any(is_safe(without_idx(s, x)) for x in range(len(s)))

if __name__ == "__main__":
    ret = 0
    while True:
        try:
            report = list(map(int, input().split()))
            if still_safe(report): ret += 1
        except:
            break
    print(ret)
