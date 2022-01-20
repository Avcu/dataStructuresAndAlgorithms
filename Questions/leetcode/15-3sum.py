## Two pointers are used for the left and right idx, and only one pointer is moved 
## based on the target and the current sum.

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result_set = set()
        
        for i in range(len(nums)):
            x1 = nums[i]
            if x1 > 0:
                break
            else:
                j = i+1
                k = len(nums)-1
                
                while j<k and j<len(nums) and k>-1:
                    x2 = nums[j]
                    x3 = nums[k]
                    if x1+x2+x3 < 0:
                        j = j + 1
                    elif x1+x2+x3 > 0:
                        k = k -1
                    else:
                        a_sol = [x1, x2, x3]
                        result_set.add(tuple(a_sol))
                        j = j + 1
                        k = k -1

                   
        return result_set