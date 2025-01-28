class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniq = sorted(list(set(nums)))
        for index, num in enumerate(uniq):
            nums[index] = num

        return len(uniq)
