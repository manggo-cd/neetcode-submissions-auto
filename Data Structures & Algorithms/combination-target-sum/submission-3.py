class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def backtrack(curr, total):
            if total == target:
                res.append(subset.copy())
                return

            if total > target:
                return

            for c in range(curr, len(nums)):
                subset.append(nums[c])
                backtrack(c, total + nums[c])
                subset.pop()

        backtrack(0, 0)
        return res