## Two pointers are used to perform binary search in a sorted array.

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        l = 0
        r = x
        
        while True:
            mid = (l+r)//2
            if mid**2 <= x and (mid+1)**2 > x:
                return mid
            elif mid*mid < x:
                l = mid + 1
            else:
                r = mid -1