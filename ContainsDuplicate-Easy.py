# Time Complexity : O(n^2)
# Space Complexity : O(1)
def containsDuplicateBrute(self, nums: list[int]) -> bool:
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Time Complexity : O(n log n)
# Space Complexity : O(1)
def containsDuplicateSort(self, nums: list[int]) -> bool:
    lp, rp = 0, 1

    nums.sort()

    while rp < len(nums):
        if nums[lp] == nums[rp]:
            return True
        else:
            lp += 1
            rp += 1
    return False

# Time Complexity : 0(n)
# Space Complexity : O(n)
def containsDuplicateHash(self, nums: list[int]) -> bool:
    hash = {}
    for i in nums:
        if i not in hash:
            hash[i] = 1
        else:
            return True
    return False

# Time Complexity : 0(n)
# Space Complexity : O(n)
def containsDuplicateSet(self, nums: list[int]) -> bool:
    return len(nums) != len(set(nums))

