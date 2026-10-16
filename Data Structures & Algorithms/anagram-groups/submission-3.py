from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        @param - strs: List[str]
        @return - grouped_anagrams : List[List[str]]
        """
        anagramsDict = {}
        for string in strs:
            sorted_key = "".join(sorted(string))
            if sorted_key not in anagramsDict:
                anagramsDict[sorted_key] = [string]
            else:
                anagramsDict[sorted_key].append(string)
        return list(anagramsDict.values())