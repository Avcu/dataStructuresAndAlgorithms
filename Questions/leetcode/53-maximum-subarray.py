## Dynamic programming is used to sole maximum subarray problem. In 1D db array, each index stores the maximum sum ending at that index.

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        db_arr = []
        for idx in range(len(nums)):
            if idx == 0:
                db_arr.append(nums[idx])
            else:
                db_arr.append(max(nums[idx], db_arr[idx-1] + nums[idx]))
        return max(db_arr)