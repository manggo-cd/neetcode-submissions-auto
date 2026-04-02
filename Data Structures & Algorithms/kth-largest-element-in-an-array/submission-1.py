class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        smallest = 0

        for i in range(len(nums) - k + 1):
            smallest = heapq.heappop(nums)

        return smallest
