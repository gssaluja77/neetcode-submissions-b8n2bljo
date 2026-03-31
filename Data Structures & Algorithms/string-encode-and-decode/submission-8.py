class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = ""
        
        for ind, word in enumerate(strs):
            encoded += str(len(word)) + "#" + word
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        decoded = []
        i = 0

        while i < len(s):
            j = i
            length = ""
            while s[j] != "#":
                length += s[j]
                j += 1
            
            decoded.append(s[j + 1 : j + 1 + int(length)])
            i = j + 1 + int(length)
        
        return decoded
