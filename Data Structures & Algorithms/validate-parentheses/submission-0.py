class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stk.append(s[i])
            elif s[i] == ")" or s[i] == "]" or s[i] == "}":
                if not stk: 
                    return False
                top = stk.pop()
                if (
                    (s[i] == ")" and top != "(") or
                    (s[i] == "]" and top != "[") or 
                    (s[i] == "}" and top != "{") 
                ):
                    return False
        if stk:
            return False
        return True