## Python built-in heaps are used.

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort(key=lambda x: x[0])
        room_heap = []
        max_count = 0
        
        for idx in range(len(intervals)):
            cur_meeting = intervals[idx]
            
            end_time = 0
            done = False
            
            # find if we can use one of the rooms created before
            if len(room_heap) > 0:
                if room_heap[0] <= cur_meeting[0]:
                    # we can use this room
                    heapq.heappop(room_heap)
                    heapq.heappush(room_heap, cur_meeting[1])
                    done = True
                    
            # could not use old rooms, so create one
            if not done:
                heapq.heappush(room_heap, cur_meeting[1])
                max_count = max(max_count, len(room_heap))
            
        return max_count