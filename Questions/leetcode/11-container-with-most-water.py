## Rather than checking all the pairs, two pointers are used for the left and right idx.
## Only the pointer corresponding to the smaller height is moved, similar to the 3-sum
## problem where only one pointer is moved based on the target and the current sum.

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_water = 0
        idx1 = 0
        idx2 = len(height) - 1
        
        cur_water = min(height[idx1],height[idx2])*(idx2-idx1)
        max_water = max(max_water, cur_water)
        while idx1<idx2:
            if height[idx1] < height[idx2]:
                new_idx = idx1+1
                while height[new_idx] < height[idx1]:
                    new_idx = new_idx + 1
                idx1 = new_idx
            else:
                new_idx = idx2-1
                while height[new_idx] < height[idx2]:
                    new_idx = new_idx - 1
                idx2 = new_idx
            cur_water = min(height[idx1],height[idx2])*(idx2-idx1)
            max_water = max(max_water, cur_water)
            #print('idx1: {} idx2:{} and water:{}'.format(idx1, idx2, cur_water))

        return max_water
        