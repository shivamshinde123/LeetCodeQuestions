class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        
        def str_freq(string):
            freq = dict()
            for char in string.lower():
                if char.isalpha() and char in licensePlate.lower():
                    freq[char] = freq.get(char, 0) + 1
                
            return freq
        
        license_plate_freq = str_freq(licensePlate)
        print(license_plate_freq)
        word_length = math.inf
        result = ""
        for word in words:
            word_freq = str_freq(word)
            print(word_freq)
            
            if all((word_freq.get(key) != None and word_freq.get(key) >= value for key, value in license_plate_freq.items())):
                print("hello {word}")
                if len(word) < word_length:
                    print("bye {word}")
                    word_length = len(word)
                    result = word
                    
        return result
        
        