class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n #masks for each word
        lens = [0] * n
        bit_number = lambda ch : ord(ch) - ord('a')
        
        for i in range(n):
            bitmask = 0
            for letter in words[i]:
                bitmask |= 1 << bit_number(letter)
            masks[i] = bitmask
            lens[i] = len(words[i]) #store length of word
            
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                #if AND result of both mask == 0 meaning not sharing common letter
                if masks[i] & masks[j] == 0:
                    res = max(res, lens[i] * lens[j])
        return res
        
    def no_common_letter(self, s1, s2):
        bit_number = lambda ch : ord(ch) - ord('a')
        
        #For masking
        bitmask1 = bitmask2 = 0
        
        for ch in s1:
            #OR the bitmask with the character bit
            bitmask1 |= 1 << bit_number(ch)
            
        for ch in s2:
            bitmask2 |= 1 << bit_number(ch)
        return bitmask1 & bitmask2 == 0
    
    