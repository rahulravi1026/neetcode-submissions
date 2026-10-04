class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.maxHeap = []
        for x, y in points:
            d = self.distanceToOrigin(x, y) * -1
            heapq.heappush(self.maxHeap, (d, [x,y]))
            if len(self.maxHeap) > k:
                heapq.heappop(self.maxHeap)
        
        result = []
        for val in self.maxHeap:
            result.append(val[1])
        return result

    def distanceToOrigin(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)

"""
only need to keep track of the k closest
-7, -4, -2
"""