class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += f"{len(string)}|" + string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "|":
                j+=1
            word_length = int(s[i:j])
            decoded.append(s[j+1 : j+1+word_length])
            i = j+1+word_length
        return decoded