class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for n in nums:
            if freq[n] > 1:
                return True

        return False