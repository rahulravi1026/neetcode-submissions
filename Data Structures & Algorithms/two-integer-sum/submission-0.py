class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        history = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in history:
                return [history[diff], i]
            history[num] = i
