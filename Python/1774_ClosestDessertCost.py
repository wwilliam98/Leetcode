class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        self.ret = float("inf")
        
        for base in baseCosts:
            self.helper(toppingCosts, target, base)
        return self.ret
        
    def helper(self, topping, target, sums):
        if abs(sums-target) < abs(self.ret-target):
            self.ret = sums
        
        if sums > target:
            return
        
        for i in range(len(topping)):
            self.helper(topping[i+1:], target, sums + 0*topping[0])
            self.helper(topping[i+1:], target, sums + 1*topping[0])
            self.helper(topping[i+1:], target, sums + 2*topping[0])
