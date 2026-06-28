class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for ind, num in enumerate(nums):
            compliment = target-num
            if compliment in hm:
                
                return sorted([ind,hm[compliment]])
            hm[num]=ind
        