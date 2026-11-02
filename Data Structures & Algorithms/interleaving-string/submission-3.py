class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n1, n2, n3 = len(s1), len(s2), len(s3)

        if n3 != n1 + n2:
            return False

        memo = {}

        # i: Index in s1, j:index in s2
        def dfs(i, j):

            if i == n1 and j == n2:
                return True

            if (i, j) in memo:
                return memo[(i, j)]

            # Index in s3
            k = i + j

            if i < n1 and s1[i] == s3[k] and dfs(i + 1, j):
                return True

            if j < n2 and s2[j] == s3[k] and dfs(i, j + 1):
                return True

            memo[(i, j)] = False
            return False


        return dfs(0, 0)