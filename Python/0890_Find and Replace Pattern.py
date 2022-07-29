class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        res = []
        cipher = {}
        
        #new character we come across is always masked to "a", the second to "b", and so on. To easily compare the words to the pattern.
        def encode(s):
            if s not in cipher:
                cipher[s] = chr(97 + len(cipher))
            return cipher[s]
        encoded = [encode(s) for s in pattern]
        
        for w in words:
            cipher = {}
            encoded_word = [encode(s) for s in w]
            if encoded == encoded_word:
                res.append(w)
        return res