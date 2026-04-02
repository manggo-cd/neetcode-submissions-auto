class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums) + 1)]
        freq = Counter(nums)
        res = []

        for n in freq:
            bucket[freq[n]].append(n)

        for group in bucket[::-1]:
            for n in group:
                res.append(n)
                if len(res) == k:
                    return res




            