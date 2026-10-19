class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        @params nums: List[int]
        @return majorityElement: int 
        """
        # Approach 1 = Hashmap Method where we count the element
        # that appears the most in the list O(N) Time O(N) Space
        elementCount = {}
        for num in nums:
            elementCount[num] = 1 +elementCount.get(num,0)
        print(elementCount)
        return max(elementCount, key = elementCount.get)
        



        