# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         f = [[True] * n for _ in range(n)]
#         k, mx = 0, 1
#         for i in range(n - 2, -1, -1):
#             for j in range(i + 1, n):
#                 f[i][j] = False
#                 if s[i] == s[j]:
#                     f[i][j] = f[i + 1][j - 1]
#                     if f[i][j] and mx < j - i + 1:
#                         k, mx = i, j - i + 1
#         return s[k : k + mx]

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def f(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l, r = l - 1, r + 1
            return r - l - 1

        n = len(s)
        start, mx = 0, 1
        for i in range(n):
            a = f(i, i)
            b = f(i, i + 1)
            t = max(a, b)
            if mx < t:
                mx = t
                start = i - ((t - 1) >> 1)
        return s[start : start + mx]
    
s = "babad"

result=Solution().longestPalindrome(s)
print(result)