class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_list = list()
        str_list = list()
        
        for char in pattern:
            pattern_list.append(pattern.index(char))
            
        for item in s.split():
            str_list.append(s.split().index(item))
            
        return pattern_list == str_list