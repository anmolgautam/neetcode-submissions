class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        i = 0

        def comb_sum(nums,target,curr,ans,i):
            if sum(curr)>target:
                    return
            if i == len(nums):
                if sum(curr)==target:
                    ans.append(curr.copy())
                    return

                if(sum(curr)!=target):
                    return

                
            
            curr.append(nums[i])
            comb_sum(nums,target,curr,ans,i)
            curr.pop()
            comb_sum(nums,target,curr,ans,i+1)
        
        comb_sum(nums,target,[],ans,0)
        return ans

        