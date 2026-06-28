class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        answer = []
        for num in nums:
            hm[num] = hm.get(num,0) + 1
        
        for key,value in hm.items():
            answer.append((value,key))
        answer = sorted(answer,reverse=True)
        #print(answer)
        ans = []
        for u,v in answer:
            ans.append(v)
        return(ans[:k])

        