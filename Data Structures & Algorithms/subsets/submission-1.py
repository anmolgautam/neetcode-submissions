class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        i = 0
        def perm(ans,nums,curr,i):
            if i==len(nums):
                #print(curr)
                ans.append(curr.copy())
                return
            
            curr.append(nums[i])
            perm(ans,nums,curr,i+1)
            curr.pop()
            perm(ans,nums,curr,i+1)
        perm(ans,nums,[],0)
        return ans
            