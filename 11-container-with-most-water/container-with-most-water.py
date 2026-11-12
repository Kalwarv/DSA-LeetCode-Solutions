class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0

        right = len(height)-1

        max_height = 0

        while left <right:
            
            wall_height = min(height[left],height[right])

            gap = right - left

            max_height = max( wall_height * gap,max_height)

            if height[left]<height[right]:

                left += 1

            else:

                right -=1

        return max_height