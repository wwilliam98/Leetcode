class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for endrow in range(len(costs)-2, -1, -1):
            costs[endrow][0] += min(costs[endrow+1][1], costs[endrow+1][2])
            costs[endrow][1] += min(costs[endrow+1][0], costs[endrow+1][2])
            costs[endrow][2] += min(costs[endrow+1][0], costs[endrow+1][1])
        
        if not costs:
            return 0
        return min(costs[0])
