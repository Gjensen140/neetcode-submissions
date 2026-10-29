class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            pre = str(len(s))
            output += pre + "#" + s
        
        return output

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)

        output = []

        while i < n:
            j = i

            while s[j] != "#":
                j += 1
            
            length = int(s[i:j])

            word = s[j + 1: j + length + 1]
            output.append(word)
            i = j + length + 1
        
        return output