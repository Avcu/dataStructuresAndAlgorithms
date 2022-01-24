class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda row: (row[0], -row[1]))
        
        result_list = []
        while len(intervals)>0:
            start_ = intervals[0][0]
            end_ = intervals[0][1]

            idx = 1
            while idx < len(intervals):
                if end_ < intervals[idx][0]:
                    break
                else:
                    end_ = max(end_, intervals[idx][1])
                    idx = idx + 1
            result_list.append([start_, end_])
            intervals = intervals[idx:]
                
        return result_list