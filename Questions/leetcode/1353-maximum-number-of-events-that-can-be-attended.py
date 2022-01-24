## Heaps are used to store the finish times of the meetings. Two indices are used as follows: 
## event_idx iterates through the meetings and adds them to the heap when they started, and
## day_counter iterates through the days, if no meeting is available we skip to the nearest 
## meeting day

import heapq

class Solution(object):
    
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """
        events = sorted(events)
        max_finish_time = max([event[1] for event in events])
        
        heap = []
        event_counter = 0
        day_counter = events[0][0]
        event_idx = 0
        
        while day_counter <= max_finish_time:
            # add the events that are started
            while event_idx < len(events) and day_counter >= events[event_idx][0]:
                heapq.heappush(heap, events[event_idx][1])
                event_idx += 1
                
            # remove the events that are passed
            while heap and day_counter > heap[0]:
                heapq.heappop(heap)
            
            # attend one event
            if heap:
                heapq.heappop(heap)
                event_counter += 1
                day_counter = day_counter+1
            elif event_idx >= len(events):
                break
            else:
                # no event in the heap, fast-forward the days
                day_counter = events[event_idx][0]

        return event_counter