class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        @param - strs : List[str]
        @return - encoded_str : str
        Our strategy to encode a string is to find the length of each word, add a special symbol after it and then append the rest of the word to a string.
        """
        encoded_str_list = []
        for word in strs:
            length = len(word)
            encoded_str_list.append(str(length)+"#"+word)
        return "".join(encoded_str_list)
        
        

    def decode(self, s: str) -> List[str]:
        """
        @param - s : str (encoded string) with #4word#pablo
        @return - decoded_str_list : List[str] should be equal to original list.

        Our approach, create a list that will contain original words and append them. We will have to traverse the string and pick out the correct words, depending on their lengths and from where they start and where they end.
        """
        decoded_list = []
        i=0

        while i < len(s):
            j= i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i= j+1
            j = i + length
            decoded_list.append(s[i:j])
            i= j
        return decoded_list

        