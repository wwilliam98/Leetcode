class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.helper(height, 0, len(height)-1, 0)
        
    def helper(self, h, left, right, area):
        while left < right:
            area = max(area, (right-left) * min(h[left], h[right]))
            if h[left] <= h[right]:
                left += 1
            else:
                right -= 1
        return area
