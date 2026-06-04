class Solution:
    def isPalindrome(self, s: str) -> bool:
        ln = len(s)
        if len(s) == 1:
            return True
        
        # s = s.lower()
        # stripped = ""
        # for i in range(ln):
        #     if s[i].isalnum():
        #         stripped += s[i]

        # ln = len(stripped)
        l = 0
        r = ln - 1

        while l<r:
            while l<r and not self.isalphaNumeric(s[l]):
                l +=1
            while l<r and not self.isalphaNumeric(s[r]):
                r -=1
            if not s[l].lower() == s[r].lower():
                return False
            l +=1
            r -=1
        return True

    def isalphaNumeric(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))
# two pointer approach



        