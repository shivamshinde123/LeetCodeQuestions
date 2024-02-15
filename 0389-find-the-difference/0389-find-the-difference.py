class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = dict()
        t_dict = dict()
        
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
        
        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        for item in t_dict:
            if (item not in s_dict) or (t_dict[item] > s_dict[item]):
                return item
                

            

            