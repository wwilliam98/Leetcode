class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k  #1000 or 4
        got = set()

        for i in range(k, len(s)+1):
            tmp = s[i-k:i]
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False
    
#Decimal Version
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        table = [0] * (2**k) #create hash table
        for i in range(k-1, len(s)):
            table[int(s[i-k+1:i+1], 2)] = 1 #save to hash table

        for i in table: #check if all hash table is 1
            if i == 0:
                return False
        return True
