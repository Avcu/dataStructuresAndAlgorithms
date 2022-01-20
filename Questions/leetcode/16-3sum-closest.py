## Very similar to original 3sum problem.

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        best_target = nums[0]+nums[1]+nums[2]
        
        for idx1 in range(len(nums)):
            x1 = nums[idx1]
            
            idx2 = idx1+1
            idx3 = len(nums)-1
            
            while idx2 < idx3 and idx2 < len(nums) and idx3>-1:
                x2 = nums[idx2]
                x3 = nums[idx3]

                res = target - x1 - x2 - x3
                if abs(res) < abs(target-best_target):
                    best_target = x1+x2+x3
                
                if res < 0:
                    idx3 = idx3-1
                elif res > 0:
                    idx2 = idx2+1
                else:
                    return best_target
        return best_target