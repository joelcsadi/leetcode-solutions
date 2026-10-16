from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        @param - strs: List[str]
        @return - grouped_anagrams : List[List[str]]
        """
        anagramsDict = defaultdict(list)
        for string in strs:
            sorted_key = "".join(sorted(string))
            anagramsDict[sorted_key].append(string)
        return list(anagramsDict.values())
            

            
        