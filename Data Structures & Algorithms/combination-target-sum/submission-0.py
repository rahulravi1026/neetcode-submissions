class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def helper(i, cur, remaining):
            if i == len(nums) or remaining < 0:
                return
            if remaining == 0:
                result.append(cur.copy())
                return
            
            helper(i, cur + [nums[i]], remaining - nums[i])
            helper(i + 1, cur, remaining)
        
        helper(0, [], target)
        return result

