class Solution:
    def frequencySort(self, s: str) -> str:
        
        ## Approach 1: using dict and sorting operation
#         freq = dict()

#         for char in s:
#             freq[char] = freq.get(char, 0) + 1
            
#         freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

#         answer = ""
#         for char in freq.keys():
#             answer += char*freq[char]
            
        # return answer
    
        ## Approach 2: with sorting operation
        freq = dict()

        for char in s:
            freq[char] = freq.get(char, 0) + 1
            
        max_freq = max(freq.values())
            
        sorted_chars = [[] for _ in range(max_freq)]
        
        for char in s:
            if char not in sorted_chars[freq[char]-1]:
                sorted_chars[freq[char]-1].append(char)
            
        answer = ""
        for i in range(max_freq,0,-1):
            answer += "".join([char*i for char in sorted_chars[i-1]])
            
        return answer
        
        
        
        