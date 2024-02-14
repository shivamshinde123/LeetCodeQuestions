class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        # Approach 1:
        # answer = list()

        # pos_stack = list()
        # neg_stack = list()

        # for elem in nums:
        #     if elem > 0:
        #         pos_stack.append(elem)
        #     else:
        #         neg_stack.append(elem)

        # for i in range(len(pos_stack)):
        #     answer.append(pos_stack[i])
        #     answer.append(neg_stack[i])

        # return answer
            
        # Approach 2:
        answer = [0] * len(nums)
        pos, neg = 0, 1

        for elem in nums:
            if elem > 0:
                answer[pos] = elem
                pos += 2
            else:
                answer[neg] = elem
                neg += 2

        return answer
