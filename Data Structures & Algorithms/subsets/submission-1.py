class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(i, cur):
            if i == len(nums):
                result.append(cur.copy())
                return 
            
            cur.append(nums[i])
            helper(i + 1, cur)
            cur.pop()
            helper(i + 1, cur)
        
        helper(0, [])
        return result
