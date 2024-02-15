class Solution:
    def frequencySort(self, s: str) -> str:
        freq = dict()

        for char in s:
            freq[char] = freq.get(char, 0) + 1
            
        freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        answer = ""
        for char in freq.keys():
            answer += char*freq[char]
            
        return answer