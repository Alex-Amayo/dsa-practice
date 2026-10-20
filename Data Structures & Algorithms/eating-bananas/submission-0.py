class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        L, R = 1, max(piles)
        res = R

        while L <= R:

            k = (L + R) // 2 
            total = 0

            for i in piles:
                total += math.ceil(i / k)

            if total <= h:
                res = k
                R = k - 1
            elif total > h:
                L = k + 1

        return res
            


                
                    
                


