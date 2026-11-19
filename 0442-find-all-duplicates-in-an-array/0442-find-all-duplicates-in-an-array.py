class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        seen = set()
        result=[]

        for nums in nums:
            if nums in seen:
                result.append(nums)
            else:
                seen.add(nums)

        return result