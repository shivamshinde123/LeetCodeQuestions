class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        # Approach 1:
        # connection = dict(zip(s, [None]*len(s)))

        # for i in range(len(s)):
        #     if connection[s[i]] != t[i]:
        #         if (connection[s[i]] == None) and (t[i] not in connection.values()):
        #             connection[s[i]] = t[i]
        #         else:
        #             return False

        # return True

        # Approach 2:
        s_pattern = list()
        t_pattern = list()

        for i in range(len(s)):
            s_pattern.append(s.index(s[i]))
            t_pattern.append(t.index(t[i]))

        if s_pattern == t_pattern:
            return True
        else:
            return False