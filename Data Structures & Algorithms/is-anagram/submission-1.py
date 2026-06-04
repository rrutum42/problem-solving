class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        if len(s) != len(t):
            return False
        for c in s:
            s_map[c] += 1
        for ch in t:
            t_map[ch] += 1
        return t_map == s_map