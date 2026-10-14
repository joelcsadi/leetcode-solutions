class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """
        @param nums: List[int]
        @return Concatenation of nums with itself List[int]

        Approach - We initialise an empty list and iterate over the nums list twice to concatenate it together by appending it Time - O(N) Space- O(N)

        In python we can also do ans = nums + nums but our method is more algorithmically univeral.
        """
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans
        