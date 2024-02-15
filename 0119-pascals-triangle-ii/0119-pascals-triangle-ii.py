class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numRows = rowIndex + 1
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]][-1]
        elif numRows == 2:
            return [[1], [1, 1]][-1]
        elif numRows > 2:
            result = [[1], [1, 1]]
            for i in range(2, numRows):
                prev_element = result[i - 1]
                temp_list = list()
                for i in range(0, len(prev_element) - 1):
                    temp_list.append(prev_element[i] + prev_element[i + 1])

                result.append([1] + temp_list + [1])

            return result[-1]
        else:
            raise Error("Incorrect numRows Entered!")