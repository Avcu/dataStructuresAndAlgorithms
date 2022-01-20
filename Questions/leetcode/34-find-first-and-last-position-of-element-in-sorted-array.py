## Two pointers are used to perform binary search in a sorted array.

class Solution(object):
    
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # find the start
        begin, end = 0, len(nums) - 1 
        final_start = -1
        while begin <= end:
            mid = (begin+end)//2

            # found the target
            if nums[mid] == target:
                if mid == begin or nums[mid-1] < target:
                    final_start = mid
                    break
                end = mid - 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid+1

        # find the end
        begin, end = 0, len(nums) - 1
        final_end = -1
        while begin <= end:
            mid = (begin+end)//2

            # found the target
            if nums[mid] == target:
                if mid == end or nums[mid+1] > target:
                    final_end = mid
                    break
                begin = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                begin = mid+1

        return [final_start, final_end]