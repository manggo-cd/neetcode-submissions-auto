class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## Two pointer

        l, r = 0, len(heights) - 1 #initialize

        rsf = 0 #accumulate

        while l < r:
            vol = (r - l) * min(heights[l], heights[r])
            rsf = max(rsf, vol)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return rsf
        

