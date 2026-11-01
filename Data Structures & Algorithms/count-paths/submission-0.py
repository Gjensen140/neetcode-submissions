class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_moves = (m + n) - 2
        options = m - 1

        numerator = 1
        for i in range(2, total_moves + 1):
            numerator *= i 

        denominator = 1

        for i in range(2, total_moves - options + 1):
            denominator *= i
        for i in range(2, options + 1):
            denominator *= i
        
        return numerator // denominator