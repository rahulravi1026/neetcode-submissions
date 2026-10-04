class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.maxHeap = []
        for x, y in points:
            d = self.distanceToOrigin(x, y) * -1
            if len(self.maxHeap) < k:
                heapq.heappush(self.maxHeap, (d, [x,y]))
            elif d > self.maxHeap[0][0]:
                heapq.heappop(self.maxHeap)
                heapq.heappush(self.maxHeap, (d, [x,y]))
        
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