class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach is to iterate to the left of and the right of the current
        # number. Accumulate the result and append to the output rsf
        n = len(nums)
        rsf = [1] * n

        l = 1
        for i in range(n):
            rsf[i] = l
            l *= nums[i]

        r = 1
        for i in range(n - 1, -1, -1):
            rsf[i] *= r
            r *= nums[i]

        return rsf




        

        