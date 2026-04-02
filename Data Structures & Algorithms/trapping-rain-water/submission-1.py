class Solution:
    def trap(self, height: List[int]) -> int:
        # curr - prev. if < 0 increment
        l, r = 0, len(height) - 1
        prevL, prevR = height[l], height[r]
        rsf = 0

        while l < r:
            if prevL < prevR:
                l += 1
                prevL = max(prevL, height[l]) # always 0 or greater
                rsf += prevL - height[l]
            else:
                r -= 1
                prevR = max(prevR, height[r])
                rsf += prevR - height[r]

        return rsf
