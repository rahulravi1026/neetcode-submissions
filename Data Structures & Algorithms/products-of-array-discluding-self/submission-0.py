class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        i, prefix = 0, 1
        while i < len(nums):
            result[i] *= prefix
            prefix *= nums[i]
            i += 1
        
        i, postfix = len(nums) - 1, 1
        while i >= 0:
            result[i] *= postfix
            postfix *= nums[i]
            i -= 1

        return result
        