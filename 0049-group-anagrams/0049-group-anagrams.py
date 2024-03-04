class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # Dictionary that keeps track of anagrams
        ana = dict() # anagram_representative : anagram list
        # for strs = ["eat","tea","tan","ate","nat","bat"], ana will be
        # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
        
        # Creating a dictionary of lists
        for element in strs:
            rearranged_ele = ''.join(sorted(element))
            if rearranged_ele not in ana:
                ana[rearranged_ele] = list()
                ana[rearranged_ele].append(element)
            else:
                ana[rearranged_ele].append(element)
                
        return ana.values()