class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        bucket = [[] for i in range(len(nums) + 1)]
        for num, freq in freq.items():
            bucket[freq].append(num)
        
        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                res.append(num)
                k -= 1
            if k == 0:
                return res
