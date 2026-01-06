class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # Sort by the difference between cost to A and cost to B
        # This tells us who benefits most from going to city A vs B
        costs.sort(key=lambda x: x[0] - x[1])
        
        n = len(costs) // 2
        total_cost = 0
        
        # First n people go to city A (they benefit most from A)
        for i in range(n):
            total_cost += costs[i][0]
        
        # Last n people go to city B
        for i in range(n, 2 * n):
            total_cost += costs[i][1]
        
        return total_cost