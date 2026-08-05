class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix sums
        
        # read once going forward 
        # read once going backward
        # O(n) + O(n)

        # multiply by the num before, update the num before, continue
        # new data structure? cant think of way to update in place

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

        



        

        