class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f'{len(s)}#{s}')
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        res, i, n = [], 0, len(s)
        while i<n:
            j = i
            while j < n and s[j] != "#":
                j += 1
            length = int(s[i:j])
            start = j+1
            end = start + length
            res.append(s[start:end])
            i=end
        return res


                
# represent the string as <len>#<str>
# ["two2#","3t"] -> "5#two2#2#3t"
# ["two2#","3t"] -> "012345678910"
# while reading read the first letter (say l)
# now read the next l+1 letters (+1 for #)
# increment i by l+1
# i = 0; n = 11; 
# length = 
    

