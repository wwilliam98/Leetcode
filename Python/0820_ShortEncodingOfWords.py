class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ret = 0
        prefix = set(words)
        for word in words:
            for i in range(1, len(word)):
                prefix.discard(word[i:])
        
        for word in prefix:
            ret += len(word) + 1
        
        return ret
