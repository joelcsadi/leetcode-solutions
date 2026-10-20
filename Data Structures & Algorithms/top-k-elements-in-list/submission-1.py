class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        @params: nums: List[int]
                 k: int
        @return K_elements :List[int]
        """

        # Approach 1 - We use a dictionary to count the frequencies of
        # the numbers and then sort the keys by the values. We then take 0:K elements. O(N) Space, O(NlogN) Time
        countMap = {}
        for num in nums:
            countMap[num] = 1+ countMap.get(num,0) 
        mapList = sorted(countMap, key = countMap.get, reverse =True)
        return mapList[ :k]

        # Apporach 2 - 

