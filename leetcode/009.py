class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x and x % 10 == 0):
            return False
        y = 0
        while y < x:
            y = y * 10 + x % 10
            x //= 10
        return x in (y, y // 10)
    

x = 121
print(Solution().isPalindrome(x))

x = -121
print(Solution().isPalindrome(x))

x = 10
print(Solution().isPalindrome(x))

x = 1001
print(Solution().isPalindrome(x))