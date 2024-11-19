def isAnagram(a: str, b: str) -> bool:
    new_b = list(b)
    for index in range(len(a)):
        if not new_b: return False
        if a[index] not in new_b: return False
        new_b.remove(a[index])
    return not new_b
def groupAnagrams(strs: list[str]) -> list[list[str]]:
    l = len(strs)
    ret = list()
    flags = [True] * l
    for index in range(l):
        if flags[index]:
            buffa = [strs[index]]
            for second_index in range(index + 1, l):
                if isAnagram(strs[index], strs[second_index]) and flags[second_index]:
                    buffa.append(strs[second_index])
                    flags[second_index] = False
            ret.append(buffa)
    return ret
assert groupAnagrams(["act","pots","tops","cat","stop","hat"]) == [["hat"],["act", "cat"],["stop", "pots", "tops"]], groupAnagrams(["act","pots","tops","cat","stop","hat"])
assert groupAnagrams(["x"]) == [["x"]], groupAnagrams(["x"])
assert groupAnagrams([""]) == [[""]], groupAnagrams([""])
