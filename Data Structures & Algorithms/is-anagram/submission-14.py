class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        @param s: str, t: str 2 lowercase strings
        @return isValidAnagram: boolean
        s= racecar
        t =carrace
        """
        # Approach 1 - Sort the words and verify if they're equal
        # O(n*log(n)+ m*log(m)) Time and O(n+m) 
        # if len(s) != len(t):
        #     return False
        # return sorted(s)==sorted(t)

        # Approach 2 - Hash {letters:frequency} in both strings and compare the dictionaries O(N) Time and O(N) Space - 2 Dictionary
        
        # if len(s) != len(t):
        #     return False
        # s_dict = {}
        # t_dict = {}
        # for letter in s:
        #     s_dict[letter] = s_dict.get(letter,0) + 1
        #     t_dict[letter] = t_dict.get(letter,0) + 1
        # return s_dict == t_dict
        
        ## Approach 3 - Use 1 dictionary/list by creating an alphabet array size 26 all initialised to 0. In the presence of a letter in s, we increment the counter, in the presence of a letter in t, we decrement the counter. If the words are the same, the letter_count list should balance out to 0 for all letters.
        if len(s) != len(t):
            return False
        letter_count = [0] * 26
        for i in range(len(s)):
            letter_count[ord(s[i]) -ord("a")] += 1
            letter_count[ord(t[i]) -ord("a")] -= 1
        return all(count == 0 for count in letter_count)
                
                