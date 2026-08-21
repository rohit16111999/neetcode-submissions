class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if len(nums) > len(set(nums)):
        #     return True
        # else:
        #     return False

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False           