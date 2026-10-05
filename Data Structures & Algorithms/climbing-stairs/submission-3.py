class Solution:
    def climbStairs(self, n: int) -> int:
        # memo = { 0 : 1 }
        # def dfs(remaining):
        #     if remaining in memo:
        #         return memo[remaining]
        #     if remaining < 0:
        #         return 0
        #     memo[remaining] = dfs(remaining - 1) + dfs(remaining - 2)
        #     return memo[remaining]
        # return dfs(n)

        if n < 2:
            return n
        
        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1] 
    

"""
1, 2, 3, 5, 8, 13
"""