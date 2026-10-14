class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        @param nums: List[int]
        @return Concatenation of nums with itself List[int]
        """

        """
        Approach - We initialise an empty 
        """
        ans = []
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
        return ans
        