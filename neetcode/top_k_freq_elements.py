def topKFrequent(nums: list[int], k: int) -> list[int]:
    num_to_freq = dict()
    freq_to_num: dict[int, list[int]]= dict()
    for num in nums:
        if num in num_to_freq:
            num_to_freq[num] += 1
        else: num_to_freq[num] = 0
    #now we make freq_to_num
    for num in num_to_freq:
        if (freq := num_to_freq[num]) in freq_to_num:
            freq_to_num[freq].append(num)
        else:
            freq_to_num[freq] = [num]
    ret = list()
    for x in sorted(freq_to_num.keys(), reverse=True):
        ret += freq_to_num[x]
    return ret[:k]

assert topKFrequent([7, 7], 1) == [7], print(topKFrequent([7, 7], 1))
assert topKFrequent([1] + [2] * 2 + [3] * 3, 2) == [2, 3], print(topKFrequent([1] + [2] * 2 + [3] * 3, 2))
