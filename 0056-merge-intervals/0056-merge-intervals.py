class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2:
            return intervals

        intervals.sort(key=lambda x: x[0])

        lst = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] > lst[-1][1]:
                lst.append(interval)
            else:
                lst[-1][1] = max(interval[1], lst[-1][1])

        return lst