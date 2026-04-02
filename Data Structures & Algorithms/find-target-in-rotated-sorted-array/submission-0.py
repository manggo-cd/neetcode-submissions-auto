class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # there is a "critical" point in a sorted array where
        # the next element is less than the previous element
        # this indicates some sort of rotation
        #   We can use binary search to search the array
        # If the middle value is greater than the right pointer
        # we know that it's been rotated and that the min value
        # is within mid to right
        # else, it's within mid to left. 
    
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]:
                if target < nums[l] or target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid + -1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1

        