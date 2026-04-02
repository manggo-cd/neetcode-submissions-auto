class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for i in range(len(nums)):
            seen[nums[i]] = 1 + seen.get(nums[i], 0)
            if seen[nums[i]] > 1:
                return True

        return False
        
         