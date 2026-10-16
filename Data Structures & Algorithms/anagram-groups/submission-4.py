from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        @param - strs: List[str]
        @return - grouped_anagrams : List[List[str]]
        """

        # Approach 1 - Sort the Strings and and add them to the dict[word] list if there exists a key with that sorted key already. O(M*NLog(N))

        # anagramsDict = {}
        # for string in strs:
        #     sorted_key = "".join(sorted(string))
        #     if sorted_key not in anagramsDict:
        #         anagramsDict[sorted_key] = [string]
        #     else:
        #         anagramsDict[sorted_key].append(string)
        # return list(anagramsDict.values())

        # Approach 2 - Remove Sorting and use a letter counter and check if its equal to that
        anagramsDict = defaultdict(list)
        for string in strs:
            frequency_list = [0] * 26
            for char in string:
                frequency_list[ord(char) - ord("a")] += 1 
            key = tuple(frequency_list)
            anagramsDict[key].append(string)
        return list(anagramsDict.values())

            