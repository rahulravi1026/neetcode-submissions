class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def helper(i, cur, remaining):
            if remaining == 0:
                result.append(cur.copy())
                return
            if i == len(candidates) or remaining < 0:
                return
            
            helper(i + 1, cur + [candidates[i]], remaining - candidates[i])
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, cur, remaining)

        helper(0, [], target)
        return result