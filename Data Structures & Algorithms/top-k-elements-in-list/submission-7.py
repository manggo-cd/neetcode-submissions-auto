class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we want to get the top k frequent
        # that calls for some sort of sorting/ ordering
        # one method that comes to mind is bucket sort
        # this includes being able store answers in buckets
        # buckets themselves can be sorted so we can iterate over our buckets to find the "top k"
        # each bucket represents a frequency, the max frequency in the worst time being the length of nums since worst case a number can occur n times for n given elements in an array

        freqMap = Counter(nums)
        res = []

        buckets = [[] for i in range(len(nums) + 1)] # skip 0?

        for num, freq in freqMap.items():
            buckets[freq].append(num)

        for i in range(len(buckets) - 1, -1, -1): # idx of current bucket
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res

        return res
            