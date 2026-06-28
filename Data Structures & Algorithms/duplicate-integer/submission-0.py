class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = set(nums)
        if len(hm)!=len(nums):
            return True
        return False
        