class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # only one person in town ==> he will be a judge
        if n == 1:
            return 1
        
        trust_freq = dict() # person: how many people trust him
        townspeople = set()
        
        for t in trust:
            townspeople.add(t[0])
            trust_freq[t[1]] = trust_freq.get(t[1],0) + 1
            
        # trust_freq_reversed =  {value:key for key,value in trust_freq.items()} # how many people trust him: person
        
        # all the people trust the potential judge i.e. n -1 people, and if judge is not present then we will get -1
        potential_judge = {value:key for key,value in trust_freq.items()}.get(n-1,-1) 
        
        # potential judge doesn't trust townspeople
        if potential_judge != -1 and potential_judge not in townspeople:
            return potential_judge
        
        return -1