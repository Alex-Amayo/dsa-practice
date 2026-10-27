class Solution:

    def encode(self, strs: List[str]) -> str:

        new_string = ""
        for s in strs:
            new_string += (str(len(s)) + "#" + s) 
        return new_string

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length ])
            i = 1 + j + length

        return res