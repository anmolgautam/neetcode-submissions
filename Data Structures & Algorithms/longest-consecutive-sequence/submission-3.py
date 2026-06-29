class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest = 0
        for ele in nums:
            
            if ele-1 not in seen:
                curr = 1
                while ele+curr in seen:
                    curr+=1

                longest = max(longest,curr)
        return longest

        
