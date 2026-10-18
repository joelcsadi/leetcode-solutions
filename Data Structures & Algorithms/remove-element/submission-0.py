class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        @param nums: List[int]
               val: int
        @return nums count not equal to value (k) : int
        """
        leftP = 0
        rightP = len(nums)-1
        while leftP <= rightP:
            if nums[leftP] == val:
                nums[leftP],nums[rightP] = nums[rightP],nums[leftP]
                rightP -= 1
            else:
                leftP +=1
        
        return leftP
            

      
            

        


        