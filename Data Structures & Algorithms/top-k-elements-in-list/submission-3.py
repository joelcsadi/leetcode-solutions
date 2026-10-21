class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        @params: nums: List[int]
                 k: int
        @return K_elements :List[int]
        """

        # Approach 1 - We use a dictionary to count the frequencies of
        # the numbers and then sort the keys by the values. We then take 0:K elements. O(N) Space, O(NlogN) Time

        # countMap = {}
        # for num in nums:
        #     countMap[num] = 1+ countMap.get(num,0) 
        # mapList = sorted(countMap, key = countMap.get, reverse =True)
        # return mapList[ :k]

        # Apporach 2 - Bucket Sort- Instead of sorting we' create another data structure. A list that uses the index as a frequency counter and each index will hold a list of numbers.
        groupCount = [[] for _ in range(len(nums)+1)]
        frequencyMap = {}

        for num in nums:
            frequencyMap[num] = 1+frequencyMap.get(num,0)
        for num,count in frequencyMap.items():
            groupCount[count].append(num)

        k_list = []

        for i in range(len(groupCount)-1,0,-1):
            for num in groupCount[i]:
                k_list.append(num)
                if len(k_list)==k:
                    return k_list



        


