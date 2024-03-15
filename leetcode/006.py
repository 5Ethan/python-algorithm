# from itertools import chain


# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows == 1:
#             return s
#         g = [[] for _ in range(numRows)]
#         i, k = 0, -1
#         for c in s:
#             g[i].append(c)
#             if i == 0 or i == numRows - 1:
#                 k = -k
#             i += k
#         return ''.join(chain(*g))


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        group = 2 * numRows - 2
        ans = []
        for i in range(1, numRows + 1):
            interval = group if i == numRows else 2 * numRows - 2 * i
            idx = i - 1
            while idx < len(s):
                ans.append(s[idx])
                idx += interval
                interval = group - interval
                if interval == 0:
                    interval = group
        return ''.join(ans)
    

s = "PAYPALISHIRING"
numRows = 4

result=Solution().convert(s,numRows)
print(result)