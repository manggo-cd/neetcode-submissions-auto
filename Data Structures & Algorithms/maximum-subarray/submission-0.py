class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = nums[0]
        curr = 0

        for n in nums:
            if curr < 0:
                curr = 0

            curr += n
            sum = max(sum, curr)

        return sum