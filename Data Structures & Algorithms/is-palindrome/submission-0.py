class Solution:
    def isPalindrome(self, s: str) -> bool:
        # O(n), O(1)
        clean = []
        for ch in s:
            if ch.isalnum():
                clean.append(ch.lower())
        s = ('').join(clean)
        
        left = 0
        right = len(s) -1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        