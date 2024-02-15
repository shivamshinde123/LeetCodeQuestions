class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # Approach 1
        pattern_list = list()
        str_list = list()
        
        for char in pattern:
            pattern_list.append(pattern.index(char))
            
        for item in s.split():
            str_list.append(s.split().index(item))
            
        return pattern_list == str_list
    
        # Approach 2
        connections = dict()
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        if len(set(pattern)) != len(set(words)):
            return False
        
        
        for i in range(len(words)):
            if words[i] in connections:
                if connections[words[i]] != pattern[i]:
                    return False
                
            else:
                connections[words[i]] = p[i]
                
        return True
        