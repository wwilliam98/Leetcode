class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = ""
        partLength = len(part)
        for i in s:
            res += i
            resLength = len(res)
            if resLength >= partLength and res[resLength - partLength: resLength+1] == part:
                res = res[:resLength-partLength]
        return res
