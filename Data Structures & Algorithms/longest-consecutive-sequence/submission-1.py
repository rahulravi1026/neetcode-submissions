class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        result, length = 0, 1

        for num in numSet:
            if num + 1 in numSet:
                continue
            while num - length in numSet:
                length += 1
            result = max(result, length)
            length = 1

        return result

            