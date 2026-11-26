class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()  # Sort the array so we can use two pointers
        result = []  # Store all unique quadruplets here

        # First loop: Select the first number
        # -3 because we need 3 more numbers after i
        for i in range(len(nums) - 3):

            # Skip duplicate first numbers to avoid repeated quadruplets
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Second loop: Select the second number
            # Start from i+1 because j must come after i
            # -2 because we need 2 more numbers after j
            for j in range(i + 1, len(nums) - 2):

                # Skip duplicate second numbers
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue

                # Third number starts just after j
                left = j + 1

                # Fourth number starts from the last index
                right = len(nums) - 1

                # Continue until the two pointers meet
                while left < right:

                    # Calculate the sum of all four selected numbers
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    # If the sum matches the target, we found a quadruplet
                    if total == target:

                        # Add these four numbers to our result
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        # Move both pointers to search for another combination
                        left += 1
                        right -= 1

                        # Skip duplicate left numbers
                        while left < right and nums[left] == nums[left-1]:
                            left += 1

                        # Skip duplicate right numbers
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1

                    # If sum is smaller than target, increase the sum
                    elif total < target:
                        left += 1

                    # If sum is greater than target, decrease the sum
                    else:
                        right -= 1

        # Return all unique quadruplets
        return result