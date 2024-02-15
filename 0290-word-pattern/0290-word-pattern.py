class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        # Approach 1
#         pattern_list = list()
#         str_list = list()
        
#         for char in pattern:
#             pattern_list.append(pattern.index(char))
            
#         for item in s.split():
#             str_list.append(s.split().index(item))
            
#         return pattern_list == str_list
    
        # Approach 2
        connections = dict() # connection dictionary maps words from s to the characters from pattern
        words = s.split()
        
        if len(pattern) != len(words):  # If length of pattern and s is not equal
            return False
        
        if len(set(pattern)) != len(set(words)): # If number of unique elements in pattern and s is not equal
            return False
        
        
        for i in range(len(words)): # If above two condions fail to execute
            if words[i] in connections:
                if connections[words[i]] != pattern[i]:
                    return False
                
            else:
                connections[words[i]] = pattern[i]
                
        return True
        