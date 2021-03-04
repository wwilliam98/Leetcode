class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        for endrow in range(1, len(costs)):
            costs[endrow][0] += min(costs[endrow-1][1], costs[endrow-1][2])
            costs[endrow][1] += min(costs[endrow-1][0], costs[endrow-1][2])
            costs[endrow][2] += min(costs[endrow-1][0], costs[endrow-1][1])
        print(costs)
        if not costs:
            return 0
        return min(costs[-1])
