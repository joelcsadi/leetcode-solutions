class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        We have a List[int] nums [4,6,8,4] and an int target as input.
        We want to return a list the indices of the 2 nums so they add up to target
        We can't use same element twice so i != j
        """
        
        """
        Approach 1 - O(N^2) Brute Force 
        """
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return[i,j]
        
        
        """
        Approach 2 - HashMap O(N) using equation manipulation
        """
        prevNums = {}
        for index, value in enumerate(nums):
            partner = target - value
            if partner in prevNums:
                return [prevNums[partner],index]
            prevNums[value] = index