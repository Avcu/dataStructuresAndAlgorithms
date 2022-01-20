## Python built-in heaps are used. Since heapq by default provides min-heap, all the numbers
## are multiplied by -1.

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        neg_nums = [-x for x in nums]
        heapq.heapify(neg_nums)
        
        for i in range(k):
            popped = heapq.heappop(neg_nums)
            
        return -popped