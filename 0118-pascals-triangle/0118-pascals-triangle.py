class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        elif numRows > 2:
            result = [[1], [1, 1]]
            for i in range(2, numRows):
                prev_element = result[i - 1]
                temp_list = list()
                for i in range(0, len(prev_element) - 1):
                    temp_list.append(prev_element[i] + prev_element[i + 1])

                result.append([1] + temp_list + [1])

            return result
        else:
            raise Error("Incorrect numRows Entered!")
