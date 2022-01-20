## Binary search is implemented in searching for the second element in the two sum problem

class Solution(object):
    
    def binSearch(self, nums, target):
        if len(nums) == 1:
            if nums[0] == target:
                return True
            return False
        else:
            mid_idx = len(nums)//2
            if nums[mid_idx] == target:
                return True
            elif nums[mid_idx] > target:
                return self.binSearch(nums[:mid_idx], target)
            else:
                return self.binSearch(nums[mid_idx:], target)
        
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        vals = []
        idx = []
        for i in range(len(sorted_nums)):
            curr = sorted_nums[i]
            if self.binSearch(sorted_nums[i+1:], target-curr):
                vals.append(curr)
                vals.append(target-curr)
                break
                
        if vals[0] == vals[1]:
            # same value is repeating
            idx.append(nums.index(vals[0]))
            rest_nums = nums[idx[0]+1:]
            idx.append(rest_nums.index(vals[1])+idx[0]+1)
        else:
            # different values
            idx.append(nums.index(vals[0]))
            idx.append(nums.index(vals[1]))
        return idx