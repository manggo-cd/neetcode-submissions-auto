class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # backtracking method 
        # iterate through given array 

        res = []

        subset = []

        #build dfs function

        def dfs(i):
            if i >= len(nums): # out of bounds
                res.append(subset.copy())
                return

            #left branch with number included

            subset.append(nums[i])
            dfs(i + 1)
            
            #right branch with no number included
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
        