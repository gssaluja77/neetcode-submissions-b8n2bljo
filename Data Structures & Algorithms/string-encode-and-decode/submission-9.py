class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        encoded = ""
        
        for ind, word in enumerate(strs):
            encoded += str(len(word)) + "¡" + word + ("|" if ind != len(strs) - 1 else "")
        
        return encoded

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        lst = s.split("|")
        decoded = []

        for item in lst:
            decoded.append(item.split("¡")[1])
        
        return decoded