class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        distinct = 0
        mxCandy = len(candyType)//2
        seen = set()
        for i in candyType:
            if i not in seen:
                distinct += 1
            seen.add(i)
        
        if distinct < mxCandy:
            return distinct
        else:
            return mxCandy
