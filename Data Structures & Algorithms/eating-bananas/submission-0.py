class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            time = 0
            for p in piles:
                time += math.ceil(p / k)
            return time <= h
        
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            if canFinish(m):
                r = m - 1
            else:
                l = m + 1
        
        return l

        

