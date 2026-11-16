class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        temp=[]
        for i in range(len(nums)):
            temp.append(nums[i]**2)
        temp.sort()

        return temp