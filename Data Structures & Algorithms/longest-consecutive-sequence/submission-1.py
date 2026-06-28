class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hm = set(nums)

        longest = 0

        for ele in nums:
            current = 0
            if ele-1 not in hm:
                current = 1
            while(ele+current in hm):
                current+=1
            longest = max(longest,current)

        return longest 

        
