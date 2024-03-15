from itertools import pairwise


class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # 而 pairwise 函数的作用是，将输入的可迭代对象转换为由相邻元素对组成的元组。
        #  这样做的目的是为了方便在迭代过程中同时访问相邻的元素。

        # sum((-1 if d[a] < d[b] else 1) * d[a] for a, b in pairwise(s)) 部分是一个生成器表达式，用于计算罗马数字每个字符对应的整数值。
        # 这里使用了一个辅助函数 pairwise，它返回一个迭代器，产生由相邻元素对组成的元组。
        # (d[s[-1]]) 是为了处理罗马数字的最后一个字符，将其对应的整数值直接加上。
        return sum((-1 if d[a] < d[b] else 1) * d[a] for a, b in pairwise(s)) + d[s[-1]]
    
print(Solution().romanToInt("III"))
print(Solution().romanToInt("LVIII"))

for a, b in pairwise("III"):
    print(a,b)