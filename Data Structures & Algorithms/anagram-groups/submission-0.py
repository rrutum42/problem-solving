class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        m = defaultdict(list)
        for s in strs:
            f = [0]*26
            for ch in s:
                f[ord(ch)-ord('a')] +=1
            m[tuple(f)].append(s)

        return list(m.values())