class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #  use bucket sort where index is count, and value is number.
        # this works because there can only be a max of len(nums) 
        # frequency (i.e. if whole list is the same num)
        # go through the bucket in descending order and append number 
        # to the rsf. if len(rsf) == k, then you have reached your answer.
        # return that list.

        count = {} # mapping the number to the index aka occurences
        freq = [[] for i in range(len(nums) + 1)] # number of empty arrays

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, c in count.items():
            freq[c].append(n)

        rsf = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                rsf.append(n)
                if len(rsf) == k:
                    return rsf



            