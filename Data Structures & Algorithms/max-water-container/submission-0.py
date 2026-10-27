class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0 
        r = len(heights) - 1
        maximum_water = 0

        while l < r:
            water = (r - l) * min(heights[r], heights[l])
            maximum_water = max(water, maximum_water)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return maximum_water




        