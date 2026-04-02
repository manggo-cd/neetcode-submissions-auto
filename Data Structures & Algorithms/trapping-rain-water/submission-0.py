class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        rsf = 0
        l, r = 0, len(height) - 1
        leftM, rightM = height[l], height[r]

        while l < r:
            if leftM < rightM:
                l += 1
                leftM = max(leftM, height[l])
                rsf += leftM - height[l]
            else:
                r -= 1
                rightM = max(rightM, height[r])
                rsf += rightM - height[r]

        return rsf


        