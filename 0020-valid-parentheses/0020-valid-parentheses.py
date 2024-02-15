class Solution:
    def isValid(self, s: str) -> bool:
        # a stack can be implemented using a list with append and pop operations
        stack = [] 
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for bracket in s:
            if bracket in pairs:
                stack.append(bracket)
            elif len(stack) == 0 or bracket != pairs[stack.pop()]:
                return False

        return len(stack) == 0
