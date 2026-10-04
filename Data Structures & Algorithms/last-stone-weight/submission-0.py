class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, stone * -1)
        
        while len(maxHeap) > 1:
            y, x = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            if x > y:
                heapq.heappush(maxHeap, y - x)

        return maxHeap[0] * -1 if maxHeap else 0


# y is the heaviest
# x is the second heaviest

# -7
# -4