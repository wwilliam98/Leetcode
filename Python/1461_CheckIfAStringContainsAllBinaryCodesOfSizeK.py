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
