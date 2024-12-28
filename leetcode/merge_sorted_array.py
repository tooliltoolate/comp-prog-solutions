def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    t = nums1[:m]
    t.extend(nums2)
    t.sort()
    for x in range(len(nums1)): nums1[x] = t[x]
