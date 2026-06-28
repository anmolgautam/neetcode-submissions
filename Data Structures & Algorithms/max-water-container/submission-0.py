class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = -float('inf')
        l=0
        r=len(heights)-1

        while(l<r):
            width = r-l
            curr_area = width * min(heights[l],heights[r])
            maxarea = max(curr_area,maxarea)
            if(heights[l]<heights[r]):
                l+=1
            else:
                r=r-1
        return maxarea
        