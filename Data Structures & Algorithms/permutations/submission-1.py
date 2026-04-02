class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])

        rsf = []
        for p in perms:
            for i in range(len(p) + 1):
                copy = p.copy()
                copy.insert(i, nums[0])
                rsf.append(copy)

        return rsf


