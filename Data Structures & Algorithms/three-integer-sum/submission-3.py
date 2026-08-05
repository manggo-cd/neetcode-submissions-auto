class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # involves two pointer
        # fix first number
        # two pointer to find the next two 
        # we break when our initial anchor passes 0, since it'll definitely surpass 0
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if n > 0:
                break

            if i > 0 and n == nums[i - 1]: # duplicate
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                currSum = n + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                
                elif currSum < 0:
                    l += 1
                
                else: 
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res