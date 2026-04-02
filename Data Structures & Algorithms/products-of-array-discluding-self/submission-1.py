class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # approach is to iterate to the left of and the right of the current
        # number. Accumulate the result and append to the output rsf
        rsf = [1] * len(nums)

        l = 1
        for i in range(len(nums)):
            rsf[i] = l
            l *= nums[i]

        r = 1
        for i in range(len(nums) - 1, -1, -1):
            rsf[i] *= r
            r *= nums[i]

        return rsf



        

        