class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ana = dict()
        
        for element in strs:
            rearranged_ele = ''.join(sorted(element))
            if rearranged_ele not in ana:
                ana[rearranged_ele] = list()
                ana[rearranged_ele].append(element)
            else:
                ana[rearranged_ele].append(element)
                
                
        
        return ana.values()