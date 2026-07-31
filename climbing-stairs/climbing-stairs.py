class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def sol(n):
            if n in memo:
                return memo[n]
            if n <=2 :
                return n
            memo[n] = sol(n-1) + sol(n-2)
            return memo[n]
        
        return sol(n)