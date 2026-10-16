class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        @param - strs: List[str]
        @return str
        """
        commonPrefix = ""
        for index in range(min(len(string) for string in strs)):
            key_char = strs[0][index]
            for word in strs:
                if strs == [] or word[index] != key_char :
                    return commonPrefix
            commonPrefix += key_char
        return commonPrefix
