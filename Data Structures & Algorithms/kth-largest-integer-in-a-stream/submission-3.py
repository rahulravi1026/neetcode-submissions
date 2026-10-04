class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        for num in nums:
            if len(self.heap) >= k:
                if num > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, num)
            else:
                heapq.heappush(self.heap, num)

    def add(self, val: int) -> int:
        print(self.heap, val)
        if len(self.heap) >= self.k:
            if val > self.heap[0]:
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        else:
            heapq.heappush(self.heap, val)
        return self.heap[0]

"""
4 5 8
"""