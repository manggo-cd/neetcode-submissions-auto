class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = [0] * len(nums)

        for n in nums:
            if seen[n - 1]:
                return n
            seen[n - 1] = 1
        return -1