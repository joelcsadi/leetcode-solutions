class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        @params: nums:List[int]
        @return containsDuplicate boolean
        We want to record if a number has been seen yet
        """

        """
        Approach 1 Brute Force O(N^2)
        We check 2 numbers in the list each time and check if they're the same number. Make sure its not the same index
        """
        # for i, i_value in enumerate(nums):
        #     for j, j_value in enumerate(nums):
        #         if i_value == j_value and i != j:
        #             return True 
        #  return False
        #  

        """
        Approach 2 - HashSet (O^N)Space and Time
        """
        memory_set = set()
        for x in nums:
            if x in memory_set:
                return True
            memory_set.add(x)
        return False

        """
        Approach 3- Sort Array and check if the number is the same
        as the neighbour O(n*Log(n))
        """
        # nums.sort()
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         return True
        # return False
