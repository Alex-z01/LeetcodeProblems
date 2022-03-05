def removeDuplicates(self, nums: list[int]) -> int:
    lp, rp = 0, 1

    while rp < len(nums):
        if nums[lp] == nums[rp]:
            del nums[rp]
        else:
            lp += 1
            rp += 1

    return len(nums)