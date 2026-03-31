class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        for k in range(1, max_bananas + 1):
            total_hours = 0
            for bananas in piles:
                if bananas < k:
                    total_hours += 1
                elif bananas%k == 0:
                    total_hours += bananas//k
                else:
                    total_hours += bananas//k + 1
            if total_hours <= h:
                return k