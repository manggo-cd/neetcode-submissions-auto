class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ## two pointer approach
        ## one left one right. the height is bottle necked by the lower of the two
        ##.     at each pointer

        ## We also need to keep track of heights so far and carry over the greatest
        ## height so far


        rsf = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            rsf = max(rsf, area)

            if heights[l] < heights[r]:
                l += 1

            else: 
                r -= 1

        return rsf
        