class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def helper(i, cur, remaining):
            if remaining == 0:
                result.append(cur.copy())
                return
            if remaining < 0 or i >= len(candidates):
                return
            
            helper(i + 1, cur + [candidates[i]], remaining - candidates[i])
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, cur, remaining)
        
        helper(0, [], target)
        return result

# [1, 2, 2, 4, 5, 6, 9]

# use 1 -- use 2, dont use 2
# dont use 1 -- use 2, dont use 2