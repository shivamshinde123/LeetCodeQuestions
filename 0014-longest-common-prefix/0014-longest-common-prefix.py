class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Approach 1
        # result = ""
        
        # for i in range(len(strs[0])):
        #     for s in strs:
        #         if i == len(s) or s[i] != strs[0][i]:
        #             return result

        #     result += strs[0][i]

        # return result

        # Appraoch 2
        result = ""

        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return result

            result += first[i]

        return result