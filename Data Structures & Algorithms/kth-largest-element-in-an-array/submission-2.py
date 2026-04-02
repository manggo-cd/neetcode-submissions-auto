class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = None

        for i in range(len(nums) - k + 1):
            res = heapq.heappop(nums)
        return res