class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        @params: nums : List[int]
        @return productOfArray : List[int]
        """

        # Approach 1 - O(N^2) Method where we multiply  
        # cumulatively,except for the current index.
        productArray = []
        
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product *= nums[j]
        #     productArray.append(product)
        # return productArray

        # Approach 2 - O(N) Time
        n = len(nums)
        prefixProductList = [1] *n
        prefixProduct = 1
        for i in range(n):
            prefixProductList[i] = prefixProduct
            prefixProduct *= nums[i]
        
        suffixProductList = [1] * n
        suffixProduct = 1
        for i in range(n-1,-1,-1):
            suffixProductList[i] = suffixProduct
            suffixProduct *= nums[i]

        productArray = []
        for i in range(len(nums)):
            productArray.append(suffixProductList[i]*prefixProductList[i])
        
        return productArray
