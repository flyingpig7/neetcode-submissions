class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = [c.lower() for c in s if c.isalnum()]
        for i in range(len(t)):
            if t[i] != t[len(t)-i-1]:
                return False
        return True