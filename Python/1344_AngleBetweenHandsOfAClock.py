class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        extra = ((hour % 12) + (minutes / 60)) * 30
        mDegree = minutes * 6
        
        diff = abs(extra - mDegree)
        return min(diff, 360-diff)
