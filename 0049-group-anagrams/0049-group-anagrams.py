class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Approach 1: Time Limit Exceeded
        # def isAnagram(s1, s2):
        #     return sorted(s1.lower()) == sorted(s2.lower())
        
        # result = list()

        # for i, s1 in enumerate(strs):
        #     temp = list()
        #     temp.append(s1)

        #     for j, s2 in enumerate(strs):
        #         if i != j:
        #             if isAnagram(s1, s2):
        #                 temp.append(s2)

        #     temp.sort()
        #     if temp not in result:
        #         result.append(temp)

        # return result

        # Approach 2
        result = defaultdict(list)

        for s in strs:
            counter = [0] * 26

            for c in s:
                counter[ord(c) - ord("a")] += 1

            result[tuple(counter)].append(s)

        return list(result.values())
