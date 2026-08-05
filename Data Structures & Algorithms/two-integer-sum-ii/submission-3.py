class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # what we want to do is have two pointers. one at start and one at the end
        # idea is that it is that the right pointer numbers is larger than 
        # the left pointers. so if the two numbers are greater than target, decrement
        # right pointer, else increment left pointer to attempt to get "closer"
        
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l + 1, r + 1]

            if currSum > target:
                r -= 1
            
            else:
                l += 1