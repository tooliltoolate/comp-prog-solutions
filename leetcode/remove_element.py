def removeElement(nums: list[int], val: int) -> int:
    #remove val, then return the number of elements that aren't val
    temp = [x for x in nums if not nums == val]
    for index, value in enumerate(temp):
        nums[index] = value
    return len(temp)

